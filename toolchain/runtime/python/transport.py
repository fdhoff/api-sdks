from __future__ import annotations

import asyncio
import inspect
import json
import threading
import logging
import re
import time
import zlib
from collections.abc import AsyncIterable, AsyncIterator, Awaitable, Callable, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from enum import Enum
from typing import (
    Any,
    Generic,
    NoReturn,
    TypeVar,
    cast,
)
from urllib.parse import parse_qs, quote, urlencode, urlsplit

import httpx
from pydantic import ValidationError
from typing_extensions import Self

from .credentials import AuthRequest, Credentials, Requirement, redact
from .errors import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext
from .model import ApiModel, parse_response, to_wire

T = TypeVar("T")

FileInput = bytes | tuple[str, bytes]
"""A file to upload: its content, or its name and content."""

# TODO: accept an async iterable in the asynchronous client, which now reads a stream synchronously.
RawBody = bytes | Iterable[bytes]
"""A raw request body: bytes, or a stream of chunks such as a file opened in binary mode. A stream is sent
once and never retried, and credentials see an empty body for it."""

_INTEGER = re.compile(r"[+-]?[0-9]+")
# The largest integer a JavaScript number holds exactly, so every runtime accepts the same numeric cursors.
_MAX_SAFE_INTEGER = 2**53 - 1
# Only gzip is decoded, and httpx would otherwise also ask for deflate, br and zstd.
_ACCEPT_ENCODING = {"Accept-Encoding": "gzip"}
# A binary body is passed on as received, so it is asked for uncompressed.
_IDENTITY = {"Accept-Encoding": "identity"}


@dataclass(frozen=True)
class Param:
    """`location` is `path`, `query`, `header`, `form` for a multipart part, or `urlencoded` for a form-encoded
    field. A `defaulted` query parameter that a call leaves out takes the client's `query_defaults` value."""

    wire: str
    name: str
    location: str
    defaulted: bool = False


@dataclass(frozen=True)
class NextLink:
    """Pages that link to the next one. Only the `params` in the link are read: it is never fetched."""

    items: str = "results"
    link: str = "next"
    params: tuple[str, ...] = ("page", "cursor")


@dataclass(frozen=True)
class Offset:
    """Pages addressed by an offset, which advances by the number of items received. Iteration ends at an
    empty page or once the offset reaches the page's `total`."""

    items: str = "results"
    total: str = "count"
    offset: str = "offset"


@dataclass(frozen=True)
class Cursor:
    """Pages that carry the next position as a value at the dotted `next` path, sent back in the `param`
    query parameter. Iteration ends when that value is null, empty or absent."""

    items: str = "results"
    next: str = "cursor"
    param: str = "cursor"


@dataclass(frozen=True)
class Operation(Generic[T]):
    id: str
    method: str
    path: str
    resource: str
    name: str
    params: tuple[Param, ...] = ()
    response: Any = None
    returns_json: bool = False
    iterator: str | None = None
    item: Any = None
    paging: NextLink | Offset | Cursor = NextLink()
    security: tuple[Requirement, ...] = ()
    host: str = ""
    binary_response: bool = False
    """A success body is bytes, returned as a download."""
    accept: str = ""
    """The media types a download is asked for in the Accept header, instead of the client's default."""
    raw_body: str = ""
    """The media type of a raw request body, sent unchanged."""
    idempotency_key: str = ""
    """The JSON body field the API deduplicates a write by. With it set, the write is retried as a GET is."""


@dataclass(frozen=True)
class Settings:
    base_url: str
    """Where an operation with no host key is sent, without a trailing slash."""
    credentials: Credentials = field(repr=False)
    headers: Mapping[str, str] = field(repr=False)
    to_error: Callable[[ErrorContext], ApiError]
    logger: logging.Logger
    timeout: float = 30.0
    max_retries: int = 3
    retry_base_delay: float = 0.5
    rate_limit_wait: float = 10.0
    max_retry_wait: float = 60.0
    hosts: Mapping[str, str] = field(default_factory=dict)
    """The base URL for each host key, without a trailing slash, as `select_hosts` returns them. An
    operation without a key goes to `base_url`."""
    header_defaults: Mapping[str, str] = field(default_factory=dict)
    """Values for header parameters that a call leaves out, by header name in any case."""
    query_defaults: Mapping[str, str] = field(default_factory=dict)
    """Values for defaulted query parameters that a call leaves out, by exact query name."""
    _defaults_by_name: dict[str, str] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "_defaults_by_name", _by_lowercase(self.header_defaults))


def _by_lowercase(defaults: Mapping[str, str]) -> dict[str, str]:
    """`defaults` keyed by lowercase name. Two names that differ only by case are an error."""
    names: dict[str, list[str]] = {}
    for name in defaults:
        names.setdefault(name.lower(), []).append(name)
    clashes = sorted(name for group in names.values() if len(group) > 1 for name in group)
    if clashes:
        raise ValueError(f"header_defaults has names that differ only by case: {', '.join(clashes)}")
    return {name.lower(): value for name, value in defaults.items()}


def select_hosts(
    environments: Mapping[str, Mapping[str, str]], environment: str, hosts: Mapping[str, str] | None = None
) -> dict[str, str]:
    """The caller's own host map, which must name exactly the keys the environments use, or else the
    named environment's. Trailing slashes are removed from every URL."""
    if hosts:
        keys = {key for urls in environments.values() for key in urls}
        missing, unknown = sorted(keys - hosts.keys()), sorted(hosts.keys() - keys)
        if missing:
            raise ValueError(f"hosts lacks keys: {', '.join(missing)}")
        if unknown:
            raise ValueError(f"hosts has unknown keys: {', '.join(unknown)}")
        return {key: url.rstrip("/") for key, url in hosts.items()}
    if environment not in environments:
        raise ValueError(f"Unknown environment {environment!r}; expected one of: {', '.join(sorted(environments))}")
    return {key: url.rstrip("/") for key, url in environments[environment].items()}


def _base_url(settings: Settings, operation: Operation[Any]) -> str:
    if not operation.host:
        return settings.base_url
    url = settings.hosts.get(operation.host)
    if url is None:
        raise ValueError(f"No base URL for host {operation.host!r}")
    return url


def _header_default(settings: Settings, wire: str) -> str | None:
    return settings._defaults_by_name.get(wire.lower())


class _Deadline(httpx.SyncByteStream):
    """Ends a body that is still arriving once the attempt is out of time."""

    def __init__(self, stream: Any, deadline: float) -> None:
        self.stream = stream
        self.deadline = deadline

    def __iter__(self) -> Iterator[bytes]:
        for chunk in self.stream:
            if time.monotonic() >= self.deadline:
                raise httpx.ReadTimeout("The attempt ran out of time")
            yield chunk

    def close(self) -> None:
        self.stream.close()


def _text(value: Any) -> str:
    if isinstance(value, Enum):
        return _text(value.value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def _field(value: Any) -> str:
    if isinstance(value, (Mapping, ApiModel)):
        return json.dumps(to_wire(value), separators=(",", ":"))
    return _text(value)


def _multipart(wire: str, value: Any) -> list[tuple[str, Any]]:
    if isinstance(value, (list, set)):
        return [part for item in value for part in _multipart(wire, item)]
    if isinstance(value, tuple):
        return [(wire, value)]
    if isinstance(value, (bytes, bytearray)):
        return [(wire, (wire, bytes(value)))]
    if isinstance(value, Mapping):
        return [(wire, (None, json.dumps(to_wire(value))))]
    return [(wire, (None, _text(value)))]


def _build_request(
    settings: Settings, operation: Operation[Any], body: Any, params: Mapping[str, Any]
) -> dict[str, Any]:
    path = operation.path
    query: list[tuple[str, str]] = []
    parts: list[tuple[str, Any]] = []
    fields: dict[str, list[str]] = {}
    headers: dict[str, str] = {}
    for param in operation.params:
        value = params.get(param.name)
        if value is None and param.location == "header":
            value = _header_default(settings, param.wire)
        elif value is None and param.defaulted:
            value = settings.query_defaults.get(param.wire)
        if value is None:
            continue
        if param.location == "header":
            headers[param.wire] = _text(value)
        elif param.location == "path":
            path = path.replace(f"{{{param.wire}}}", quote(_text(value), safe=""))
        elif param.location == "query":
            items = value if isinstance(value, (list, set)) else [value]
            query.extend((param.wire, _text(item)) for item in items)
        elif param.location == "urlencoded":
            items = value if isinstance(value, (list, set)) else [value]
            fields.setdefault(param.wire, []).extend(_field(item) for item in items)
        else:
            parts.extend(_multipart(param.wire, value))
    search = f"?{urlencode(query)}" if query else ""
    request: dict[str, Any] = {
        "method": operation.method,
        "url": f"{_base_url(settings, operation)}{path}{search}",
        "headers": {**headers, **(_IDENTITY if operation.binary_response else _ACCEPT_ENCODING)},
    }
    if operation.accept:
        request["headers"]["Accept"] = operation.accept
    if parts:
        request["files"] = parts
    elif fields:
        request["data"] = fields
    elif operation.raw_body:
        request["content"] = bytes(body) if isinstance(body, (bytearray, memoryview)) else body
        request["headers"]["Content-Type"] = operation.raw_body
    elif body is not None:
        request["json"] = to_wire(body)
    return request


@dataclass(frozen=True)
class _Reply:
    """A decoded success body, with the text it came from for errors."""

    data: Any
    text: str
    status: int


def _log(settings: Settings, level: int, message: str) -> None:
    settings.logger.log(level, "%s", redact(settings.credentials, message))


def _parse_json(text: str) -> Any:
    try:
        return json.loads(text)
    except ValueError:
        return None


def _read(settings: Settings, operation: Operation[Any], response: httpx.Response) -> _Reply:
    text = response.text
    _log(settings, logging.DEBUG, f"<- {operation.method} {response.status_code} ({len(text)} chars)")
    if not response.is_success:
        clean = redact(settings.credentials, text)
        raise settings.to_error(ErrorContext(response.status_code, response.headers, clean, _parse_json(clean)))
    status = response.status_code
    if status == 204:
        return _Reply(None, text, status)
    if text == "":
        if operation.returns_json:
            raise DecodeError("The response body is empty", status=status)
        return _Reply("" if operation.response is str else None, text, status)
    if "json" not in response.headers.get("content-type", ""):
        return _Reply(text, text, status)
    try:
        return _Reply(json.loads(text), text, status)
    except ValueError:
        raise DecodeError("The response body is not valid JSON", status=status) from None


def _is_stream(operation: Operation[Any], body: Any) -> bool:
    """A raw body that is not bytes can be read only once."""
    return bool(operation.raw_body) and body is not None and not isinstance(body, (bytes, bytearray, memoryview))


async def _async_chunks(chunks: Iterable[bytes]) -> AsyncIterator[bytes]:
    for chunk in chunks:
        yield chunk


class Download:
    """A binary response body, read as it arrives. The attempt's deadline keeps running while it is read.
    Close it, or use it as a context manager."""

    def __init__(self, response: httpx.Response, chunks: Iterable[bytes]) -> None:
        self._response = response
        self._chunks = chunks
        self.content_type: str = response.headers.get("content-type", "")
        """The response's `Content-Type`, or empty if it has none."""

    def iter_bytes(self) -> Iterator[bytes]:
        """Yield the body in chunks as they arrive. It can be read only once."""
        try:
            for chunk in self._chunks:
                if chunk:
                    yield chunk
        except httpx.TransportError as error:
            raise _translate(error) from error
        finally:
            self.close()

    def read(self) -> bytes:
        """The whole body."""
        return b"".join(self.iter_bytes())

    def close(self) -> None:
        self._response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncDownload:
    """A binary response body, read as it arrives. The attempt's deadline keeps running while it is read.
    Close it, or use it as an asynchronous context manager."""

    def __init__(self, response: httpx.Response, deadline: float) -> None:
        self._response = response
        self._deadline = deadline
        self.content_type: str = response.headers.get("content-type", "")
        """The response's `Content-Type`, or empty if it has none."""

    async def aiter_bytes(self) -> AsyncIterator[bytes]:
        """Yield the body in chunks as they arrive. It can be read only once."""
        chunks = aiter(cast(httpx.AsyncByteStream, self._response.stream))
        loop = asyncio.get_running_loop()
        try:
            while True:
                remaining = self._deadline - loop.time()
                if remaining <= 0:
                    raise ApiTimeoutError("The request timed out")
                try:
                    chunk = await asyncio.wait_for(anext(chunks), remaining)
                except StopAsyncIteration:
                    return
                except asyncio.TimeoutError as error:
                    raise ApiTimeoutError("The request timed out") from error
                except httpx.TransportError as error:
                    raise _translate(error) from error
                if chunk:
                    yield chunk
        finally:
            await self.aclose()

    async def aread(self) -> bytes:
        """The whole body."""
        return b"".join([chunk async for chunk in self.aiter_bytes()])

    async def aclose(self) -> None:
        await self._response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()


def _undecodable(response: httpx.Response) -> httpx.Response:
    """A success response has no result to give. Any other status still maps to its error, with no body."""
    if response.is_success:
        raise DecodeError("The response body could not be decompressed", status=response.status_code)
    headers = response.headers.copy()
    headers.pop("content-encoding", None)
    return httpx.Response(response.status_code, headers=headers)


def _gunzip(data: bytes) -> bytes:
    """Read every gzip member, and fail on a body cut short, which httpx accepts."""
    parts: list[bytes] = []
    while data:
        decoder = zlib.decompressobj(zlib.MAX_WBITS | 16)
        parts.append(decoder.decompress(data))
        if not decoder.eof:
            raise zlib.error("The gzip body ends early")
        data = decoder.unused_data
    return b"".join(parts)


def _decoded(response: httpx.Response, raw: bytes) -> httpx.Response:
    headers = response.headers.copy()
    try:
        if raw and headers.get("content-encoding", "").strip().lower() == "gzip":
            raw = _gunzip(raw)
            del headers["content-encoding"]
        return httpx.Response(response.status_code, headers=headers, content=raw)
    except (zlib.error, httpx.DecodingError):
        return _undecodable(response)


def _translate(error: httpx.TransportError) -> ApiError:
    if isinstance(error, httpx.TimeoutException):
        return ApiTimeoutError("The request timed out")
    return ApiConnectionError(f"The connection failed: {type(error).__name__}")


def _retry_after(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if value.isascii() and value.isdigit():
        return float(value)
    try:
        when = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    wait: float = (when - datetime.now(timezone.utc)).total_seconds()
    return wait if wait > 0 else None


def _repeatable(operation: Operation[Any], request: Mapping[str, Any]) -> bool:
    """A GET, or a write whose body carries the key the API deduplicates it by. A key left empty is not one."""
    if operation.method == "GET":
        return True
    body = request.get("json")
    key = operation.idempotency_key
    return bool(key) and isinstance(body, Mapping) and body.get(key) not in (None, "")


def _retry_delay(settings: Settings, error: ApiError, repeatable: bool, tries: int) -> float | None:
    if tries >= settings.max_retries:
        return None
    if error.status == 429:
        wait = _retry_after(error.retry_after)
        if wait is None:
            return settings.rate_limit_wait
        return wait if wait <= settings.max_retry_wait else None
    failed = isinstance(error, (ApiTimeoutError, ApiConnectionError)) or (error.status or 0) >= 500
    if repeatable and failed:
        return float(settings.retry_base_delay * 2**tries)
    return None


def _query_names(operation: Operation[Any]) -> dict[str, str]:
    return {param.wire: param.name for param in operation.params if param.location == "query"}


def _next_link(
    operation: Operation[Any], paging: NextLink, params: dict[str, Any], page: Mapping[str, Any]
) -> dict[str, Any] | None:
    """Read the position out of the link and apply it to our own request. The link is never fetched:
    it could send the credential to another host."""
    if not isinstance(page.get(paging.items), list):
        raise DecodeError(f"The `{paging.items}` field of a page is not a list")
    link = page.get(paging.link)
    if not link:
        return None
    try:
        position = parse_qs(urlsplit(str(link)).query)
    except ValueError:
        raise DecodeError(f"The `{paging.link}` link is not a valid URL") from None
    names = _query_names(operation)
    updated = dict(params)
    for wire in paging.params:
        if wire in position and wire in names:
            updated[names[wire]] = position[wire][0]
    if all(str(updated.get(name)) == str(params.get(name)) for name in names.values()):
        raise DecodeError(f"The `{paging.link}` link does not advance the iteration")
    return updated


def _next_offset(
    operation: Operation[Any], paging: Offset, params: dict[str, Any], page: Mapping[str, Any], received: int
) -> dict[str, Any] | None:
    if not isinstance(page.get(paging.items), list):
        raise DecodeError(f"The `{paging.items}` field of a page is not a list")
    if received == 0:
        return None
    name = _query_names(operation)[paging.offset]
    current = params.get(name)
    start = _text(current) if current is not None else "0"
    if not _INTEGER.fullmatch(start):
        raise DecodeError(f"The `{paging.offset}` parameter is not an integer")
    position = int(start) + received
    total = page.get(paging.total)
    if isinstance(total, (int, float)) and not isinstance(total, bool) and position >= total:
        return None
    return {**params, name: position}


def _next_cursor(
    operation: Operation[Any], paging: Cursor, params: dict[str, Any], page: Mapping[str, Any]
) -> dict[str, Any] | None:
    if not isinstance(page.get(paging.items), list):
        raise DecodeError(f"The `{paging.items}` field of a page is not a list")
    value: Any = page
    for key in paging.next.split("."):
        if value is None:
            break
        if not isinstance(value, Mapping):
            raise DecodeError(f"The `{paging.next}` value of a page is not inside an object")
        value = value.get(key)
    if value is None or value == "":
        return None
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and abs(value) <= _MAX_SAFE_INTEGER
        and value == int(value)
    ):
        value = str(int(value))
    if not isinstance(value, str):
        raise DecodeError(f"The `{paging.next}` value of a page is not a string or an integer")
    name = _query_names(operation)[paging.param]
    current = params.get(name)
    if current is not None and _text(current) == value:
        raise DecodeError(f"The `{paging.next}` value does not advance the iteration")
    return {**params, name: value}


def _next_params(operation: Operation[Any], params: dict[str, Any], page: Any, received: int) -> dict[str, Any] | None:
    """The parameters of the page after this one, or None after the last."""
    if not isinstance(page, Mapping):
        raise DecodeError("A page is not a JSON object")
    paging = operation.paging
    if isinstance(paging, Offset):
        return _next_offset(operation, paging, params, page, received)
    if isinstance(paging, Cursor):
        return _next_cursor(operation, paging, params, page)
    return _next_link(operation, paging, params, page)


def _auth_request(operation: Operation[Any], outgoing: httpx.Request, body: bytes) -> AuthRequest:
    return AuthRequest(operation.method, str(outgoing.url), outgoing.headers.copy(), body, operation)


def _signed(outgoing: httpx.Request, auth: AuthRequest) -> httpx.Request:
    outgoing.headers = httpx.Headers(auth.headers)
    return outgoing


def _sync(value: Any, method: str) -> Any:
    if inspect.isawaitable(value):
        if inspect.iscoroutine(value):
            value.close()
        raise TypeError(f"Credentials.{method} returned an awaitable, which only the asynchronous client accepts")
    return value


async def _settle(value: Any) -> Any:
    return await value if inspect.isawaitable(value) else value


def _unauthorized(operation: Operation[Any], error: ApiError, refreshed: bool) -> bool:
    """Only once per call, and never for an operation that sends no credentials, such as a token request
    made during a refresh."""
    return error.status == 401 and not refreshed and bool(operation.security)


def _raise_failure(settings: Settings, operation: Operation[Any], response: httpx.Response) -> NoReturn:
    """Raise the error for a failure response that a download has read whole."""
    _read(settings, operation, response)
    raise AssertionError("A failure response maps to an error")


def _opened(settings: Settings, operation: Operation[Any], response: httpx.Response) -> None:
    _log(settings, logging.DEBUG, f"<- {operation.method} {response.status_code} (streamed)")


R = TypeVar("R")


class SyncTransport:
    def __init__(self, settings: Settings, http_transport: httpx.BaseTransport | None = None) -> None:
        self.settings = settings
        self.http = httpx.Client(timeout=settings.timeout, headers=dict(settings.headers), transport=http_transport)
        self._refresh_lock = threading.Lock()
        self._generations: dict[str, int] = {}

    def _refresh(self, auth: AuthRequest, group: str, generation: int) -> bool:
        """Calls waiting on a refresh of the same group share it, and a call whose credentials were
        refreshed since it sent them retries without another."""
        with self._refresh_lock:
            if self._generations.get(group, 0) != generation:
                return True
            refreshed = bool(_sync(self.settings.credentials.refresh(auth), "refresh"))
            if refreshed:
                self._generations[group] = generation + 1
            return refreshed

    # TODO: httpx has no deadline of its own and a blocking read cannot be interrupted, so the deadline
    # is checked as each chunk arrives. A stalled read can overrun it by one timeout, and headers that
    # trickle are not caught. Closing that gap needs a worker thread or a custom network backend.
    def _attempt(self, outgoing: httpx.Request) -> httpx.Response:
        deadline = time.monotonic() + self.settings.timeout
        response = self.http.send(outgoing, stream=True)
        try:
            # The stream itself, because iter_raw refuses a body that was read already, as a mock transport's is.
            return _decoded(response, b"".join(_Deadline(response.stream, deadline)))
        finally:
            response.close()

    def _open(self, operation: Operation[Any], outgoing: httpx.Request) -> Download:
        """A success response is handed over unread, with the deadline still running. A failure is read whole."""
        deadline = time.monotonic() + self.settings.timeout
        response = self.http.send(outgoing, stream=True)
        if response.is_success:
            _opened(self.settings, operation, response)
            return Download(response, _Deadline(response.stream, deadline))
        try:
            failure = _decoded(response, b"".join(_Deadline(response.stream, deadline)))
        finally:
            response.close()
        _raise_failure(self.settings, operation, failure)

    def fetch(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> _Reply:
        return self._send(
            operation, body, params, lambda outgoing: _read(self.settings, operation, self._attempt(outgoing))
        )

    def download(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> Download:
        return self._send(operation, body, params, lambda outgoing: self._open(operation, outgoing))

    def _send(
        self,
        operation: Operation[Any],
        body: Any,
        params: Mapping[str, Any],
        attempt: Callable[[httpx.Request], R],
    ) -> R:
        settings = self.settings
        request = _build_request(settings, operation, body, params)
        streamed = _is_stream(operation, body)
        repeatable = _repeatable(operation, request)
        tries = 0
        refreshed = False
        while True:
            _log(settings, logging.DEBUG, f"-> {request['method']} {request['url']}")
            group = settings.credentials.refresh_group(operation)
            generation = self._generations.get(group, 0)
            outgoing = self.http.build_request(**request)
            auth = _auth_request(operation, outgoing, b"" if streamed else outgoing.read())
            _sync(settings.credentials.apply(auth), "apply")
            try:
                try:
                    return attempt(_signed(outgoing, auth))
                except httpx.TransportError as error:
                    raise _translate(error) from error
            except ApiError as error:
                # A stream has been read, so it cannot be sent again.
                if streamed:
                    raise
                if _unauthorized(operation, error, refreshed):
                    refreshed = True
                    if self._refresh(auth, group, generation):
                        _log(settings, logging.INFO, "retrying after refreshing credentials")
                        continue
                delay = _retry_delay(settings, error, repeatable, tries)
                if delay is None:
                    raise
                _log(settings, logging.INFO, f"retrying after {delay}s: {error.kind}")
                time.sleep(delay)
                tries += 1


class AsyncTransport:
    def __init__(self, settings: Settings, http_transport: httpx.AsyncBaseTransport | None = None) -> None:
        self.settings = settings
        self.http = httpx.AsyncClient(
            timeout=settings.timeout, headers=dict(settings.headers), transport=http_transport
        )
        self._refresh_lock = asyncio.Lock()
        self._generations: dict[str, int] = {}

    async def _refresh(self, auth: AuthRequest, group: str, generation: int) -> bool:
        """Calls waiting on a refresh of the same group share it, and a call whose credentials were
        refreshed since it sent them retries without another."""
        async with self._refresh_lock:
            if self._generations.get(group, 0) != generation:
                return True
            refreshed = bool(await _settle(self.settings.credentials.refresh(auth)))
            if refreshed:
                self._generations[group] = generation + 1
            return refreshed

    async def _attempt(self, outgoing: httpx.Request) -> httpx.Response:
        response = await self.http.send(outgoing, stream=True)
        try:
            stream = cast(httpx.AsyncByteStream, response.stream)
            return _decoded(response, b"".join([chunk async for chunk in stream]))
        finally:
            await response.aclose()

    async def _fetch_attempt(self, operation: Operation[Any], outgoing: httpx.Request) -> _Reply:
        try:
            response = await asyncio.wait_for(self._attempt(outgoing), self.settings.timeout)
        except asyncio.TimeoutError as error:
            raise ApiTimeoutError("The request timed out") from error
        return _read(self.settings, operation, response)

    async def _open(self, operation: Operation[Any], outgoing: httpx.Request) -> AsyncDownload:
        """A success response is handed over unread, with the deadline still running. A failure is read whole."""
        settings = self.settings
        deadline = asyncio.get_running_loop().time() + settings.timeout
        try:
            response = await asyncio.wait_for(self.http.send(outgoing, stream=True), settings.timeout)
        except asyncio.TimeoutError as error:
            raise ApiTimeoutError("The request timed out") from error
        if response.is_success:
            _opened(settings, operation, response)
            return AsyncDownload(response, deadline)
        try:
            stream = cast(httpx.AsyncByteStream, response.stream)
            remaining = max(deadline - asyncio.get_running_loop().time(), 0)
            raw = await asyncio.wait_for(_collect(stream), remaining)
        except asyncio.TimeoutError as error:
            raise ApiTimeoutError("The request timed out") from error
        finally:
            await response.aclose()
        _raise_failure(settings, operation, _decoded(response, raw))

    async def fetch(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> _Reply:
        return await self._send(operation, body, params, lambda outgoing: self._fetch_attempt(operation, outgoing))

    async def download(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> AsyncDownload:
        return await self._send(operation, body, params, lambda outgoing: self._open(operation, outgoing))

    async def _send(
        self,
        operation: Operation[Any],
        body: Any,
        params: Mapping[str, Any],
        attempt: Callable[[httpx.Request], Awaitable[R]],
    ) -> R:
        settings = self.settings
        streamed = _is_stream(operation, body)
        if streamed and not isinstance(body, AsyncIterable):
            body = _async_chunks(body)
        request = _build_request(settings, operation, body, params)
        repeatable = _repeatable(operation, request)
        tries = 0
        refreshed = False
        while True:
            _log(settings, logging.DEBUG, f"-> {request['method']} {request['url']}")
            group = settings.credentials.refresh_group(operation)
            generation = self._generations.get(group, 0)
            outgoing = self.http.build_request(**request)
            auth = _auth_request(operation, outgoing, b"" if streamed else await outgoing.aread())
            await _settle(settings.credentials.apply(auth))
            try:
                try:
                    return await attempt(_signed(outgoing, auth))
                except httpx.TransportError as error:
                    raise _translate(error) from error
            except ApiError as error:
                # A stream has been read, so it cannot be sent again.
                if streamed:
                    raise
                if _unauthorized(operation, error, refreshed):
                    refreshed = True
                    if await self._refresh(auth, group, generation):
                        _log(settings, logging.INFO, "retrying after refreshing credentials")
                        continue
                delay = _retry_delay(settings, error, repeatable, tries)
                if delay is None:
                    raise
                _log(settings, logging.INFO, f"retrying after {delay}s: {error.kind}")
                await asyncio.sleep(delay)
                tries += 1


async def _collect(stream: httpx.AsyncByteStream) -> bytes:
    return b"".join([chunk async for chunk in stream])


def _parse(settings: Settings, response_type: Any, data: Any, reply: _Reply) -> Any:
    """Inside an object, a field that does not fit keeps its raw value. A body that does not fit at all is an error.
    A 204 has no result, though many operations that answer it also declare a JSON success."""
    if reply.status == 204:
        return None
    try:
        return parse_response(response_type, data)
    except ValidationError:
        clean = redact(settings.credentials, reply.text)
        raise DecodeError(
            "The response body does not fit its declared type", status=reply.status, raw_body=clean
        ) from None


def _items(operation: Operation[Any], page: Any) -> Sequence[Any]:
    results = page.get(operation.paging.items) if isinstance(page, Mapping) else None
    return results if isinstance(results, list) else []


class Resource:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def _call(self, operation: Operation[T], /, *, _body: Any = None, **params: Any) -> T:
        reply = self._transport.fetch(operation, _body, params)
        result: T = _parse(self._transport.settings, operation.response, reply.data, reply)
        return result

    def _download(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> Download:
        return self._transport.download(operation, _body, params)

    def _paginate(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> Iterator[Any]:
        current: dict[str, Any] | None = params
        while current is not None:
            page = self._transport.fetch(operation, _body, current)
            if page.status == 204:
                return
            items = _items(operation, page.data)
            for item in items:
                yield _parse(self._transport.settings, operation.item, item, page)
            current = _next_params(operation, current, page.data, len(items))


class AsyncResource:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def _call(self, operation: Operation[T], /, *, _body: Any = None, **params: Any) -> T:
        reply = await self._transport.fetch(operation, _body, params)
        result: T = _parse(self._transport.settings, operation.response, reply.data, reply)
        return result

    async def _download(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> AsyncDownload:
        return await self._transport.download(operation, _body, params)

    async def _paginate(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> AsyncIterator[Any]:
        current: dict[str, Any] | None = params
        while current is not None:
            page = await self._transport.fetch(operation, _body, current)
            if page.status == 204:
                return
            items = _items(operation, page.data)
            for item in items:
                yield _parse(self._transport.settings, operation.item, item, page)
            current = _next_params(operation, current, page.data, len(items))
