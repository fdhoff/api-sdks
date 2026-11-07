from __future__ import annotations

import asyncio
import json
import logging
import time
import zlib
from collections.abc import AsyncIterator, Callable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from enum import Enum
from typing import (
    Any,
    Generic,
    TypeVar,
    cast,
)
from urllib.parse import parse_qs, quote, urlencode, urlsplit

import httpx
from pydantic import ValidationError

from .errors import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext
from .model import parse_response, to_wire

T = TypeVar("T")

FileInput = bytes | tuple[str, bytes]
"""A file to upload: its content, or its name and content."""

_REDACTED = "***"
_PAGE_MARKERS = ("page", "cursor")
# Only gzip is decoded, and httpx would otherwise also ask for deflate, br and zstd.
_ACCEPT_ENCODING = {"Accept-Encoding": "gzip"}


@dataclass(frozen=True)
class Param:
    wire: str
    name: str
    location: str


@dataclass(frozen=True)
class Operation(Generic[T]):
    id: str
    method: str
    path: str
    resource: str
    name: str
    params: tuple[Param, ...] = ()
    response: Any = None
    iterator: str | None = None
    item: Any = None


@dataclass(frozen=True)
class Settings:
    base_url: str
    secret: str = field(repr=False)
    headers: Mapping[str, str] = field(repr=False)
    to_error: Callable[[ErrorContext], ApiError]
    logger: logging.Logger
    timeout: float = 30.0
    max_retries: int = 3
    retry_base_delay: float = 0.5
    rate_limit_wait: float = 10.0
    max_retry_wait: float = 60.0


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
    for param in operation.params:
        value = params.get(param.name)
        if value is None:
            continue
        if param.location == "path":
            path = path.replace(f"{{{param.wire}}}", quote(_text(value), safe=""))
        elif param.location == "query":
            items = value if isinstance(value, (list, set)) else [value]
            query.extend((param.wire, _text(item)) for item in items)
        else:
            parts.extend(_multipart(param.wire, value))
    search = f"?{urlencode(query)}" if query else ""
    request: dict[str, Any] = {"method": operation.method, "url": f"{settings.base_url}{path}{search}"}
    if parts:
        request["files"] = parts
    elif body is not None:
        request["json"] = to_wire(body)
    return request


def _log(settings: Settings, level: int, message: str) -> None:
    settings.logger.log(level, "%s", message.replace(settings.secret, _REDACTED))


def _parse_json(text: str) -> Any:
    try:
        return json.loads(text)
    except ValueError:
        return None


def _read(settings: Settings, operation: Operation[Any], response: httpx.Response) -> Any:
    text = response.text
    _log(settings, logging.DEBUG, f"<- {operation.method} {response.status_code} ({len(text)} chars)")
    if not response.is_success:
        clean = text.replace(settings.secret, _REDACTED)
        raise settings.to_error(ErrorContext(response.status_code, response.headers, clean, _parse_json(clean)))
    if text == "":
        if operation.response not in (None, str):
            raise DecodeError("The response body is empty", status=response.status_code)
        return "" if operation.response is str else None
    if "json" not in response.headers.get("content-type", ""):
        return text
    try:
        return json.loads(text)
    except ValueError:
        raise DecodeError("The response body is not valid JSON", status=response.status_code) from None


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


def _retry_delay(settings: Settings, error: ApiError, method: str, tries: int) -> float | None:
    if tries >= settings.max_retries:
        return None
    if error.status == 429:
        wait = _retry_after(error.retry_after)
        if wait is None:
            return settings.rate_limit_wait
        return wait if wait <= settings.max_retry_wait else None
    failed = isinstance(error, (ApiTimeoutError, ApiConnectionError)) or (error.status or 0) >= 500
    if method == "GET" and failed:
        return float(settings.retry_base_delay * 2**tries)
    return None


def _next_params(operation: Operation[Any], params: dict[str, Any], page: Any) -> dict[str, Any] | None:
    """Read the position out of `next` and apply it to our own request. `next` is never fetched:
    it could send the credential to another host."""
    if not isinstance(page, Mapping):
        raise DecodeError("A page is not a JSON object")
    link = page.get("next")
    if not link:
        return None
    try:
        position = parse_qs(urlsplit(str(link)).query)
    except ValueError:
        raise DecodeError("The `next` link is not a valid URL") from None
    names = {param.wire: param.name for param in operation.params if param.location == "query"}
    updated = dict(params)
    for wire in _PAGE_MARKERS:
        if wire in position and wire in names:
            updated[names[wire]] = position[wire][0]
    if all(str(updated.get(name)) == str(params.get(name)) for name in names.values()):
        raise DecodeError("The `next` link does not advance the iteration")
    return updated


class SyncTransport:
    def __init__(self, settings: Settings, http_transport: httpx.BaseTransport | None = None) -> None:
        self.settings = settings
        self.http = httpx.Client(timeout=settings.timeout, headers=dict(settings.headers), transport=http_transport)

    # TODO: httpx has no deadline of its own and a blocking read cannot be interrupted, so the deadline
    # is checked as each chunk arrives. A stalled read can overrun it by one timeout, and headers that
    # trickle are not caught. Closing that gap needs a worker thread or a custom network backend.
    def _attempt(self, request: dict[str, Any]) -> httpx.Response:
        deadline = time.monotonic() + self.settings.timeout
        with self.http.stream(**request, headers=_ACCEPT_ENCODING) as response:
            # The stream itself, because iter_raw refuses a body that was read already, as a mock transport's is.
            return _decoded(response, b"".join(_Deadline(response.stream, deadline)))

    def fetch(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> Any:
        settings = self.settings
        request = _build_request(settings, operation, body, params)
        tries = 0
        while True:
            _log(settings, logging.DEBUG, f"-> {request['method']} {request['url']}")
            try:
                try:
                    response = self._attempt(request)
                except httpx.TransportError as error:
                    raise _translate(error) from error
                return _read(settings, operation, response)
            except ApiError as error:
                delay = _retry_delay(settings, error, operation.method, tries)
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

    async def _attempt(self, request: dict[str, Any]) -> httpx.Response:
        async with self.http.stream(**request, headers=_ACCEPT_ENCODING) as response:
            stream = cast(httpx.AsyncByteStream, response.stream)
            return _decoded(response, b"".join([chunk async for chunk in stream]))

    async def fetch(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> Any:
        settings = self.settings
        request = _build_request(settings, operation, body, params)
        tries = 0
        while True:
            _log(settings, logging.DEBUG, f"-> {request['method']} {request['url']}")
            try:
                try:
                    response = await asyncio.wait_for(self._attempt(request), settings.timeout)
                except httpx.TransportError as error:
                    raise _translate(error) from error
                except asyncio.TimeoutError as error:
                    raise ApiTimeoutError("The request timed out") from error
                return _read(settings, operation, response)
            except ApiError as error:
                delay = _retry_delay(settings, error, operation.method, tries)
                if delay is None:
                    raise
                _log(settings, logging.INFO, f"retrying after {delay}s: {error.kind}")
                await asyncio.sleep(delay)
                tries += 1


def _parse(settings: Settings, response_type: Any, data: Any) -> Any:
    """Inside an object, a field that does not fit keeps its raw value. A body that does not fit at all is an error."""
    try:
        return parse_response(response_type, data)
    except ValidationError:
        raw = data if data is None or isinstance(data, str) else json.dumps(data)
        clean = None if raw is None else raw.replace(settings.secret, _REDACTED)
        raise DecodeError("The response body does not fit its declared type", raw_body=clean) from None


def _items(page: Any) -> Sequence[Any]:
    results = page.get("results") if isinstance(page, Mapping) else None
    return results if isinstance(results, list) else []


class Resource:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def _call(self, operation: Operation[T], /, *, _body: Any = None, **params: Any) -> T:
        data = self._transport.fetch(operation, _body, params)
        result: T = _parse(self._transport.settings, operation.response, data)
        return result

    def _paginate(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> Iterator[Any]:
        current: dict[str, Any] | None = params
        while current is not None:
            page = self._transport.fetch(operation, _body, current)
            for item in _items(page):
                yield _parse(self._transport.settings, operation.item, item)
            current = _next_params(operation, current, page)


class AsyncResource:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def _call(self, operation: Operation[T], /, *, _body: Any = None, **params: Any) -> T:
        data = await self._transport.fetch(operation, _body, params)
        result: T = _parse(self._transport.settings, operation.response, data)
        return result

    async def _paginate(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> AsyncIterator[Any]:
        current: dict[str, Any] | None = params
        while current is not None:
            page = await self._transport.fetch(operation, _body, current)
            for item in _items(page):
                yield _parse(self._transport.settings, operation.item, item)
            current = _next_params(operation, current, page)
