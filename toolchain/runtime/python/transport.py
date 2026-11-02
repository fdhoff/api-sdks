from __future__ import annotations

import asyncio
import json
import logging
import time
from collections.abc import AsyncIterator, Callable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from enum import Enum
from typing import (
    Any,
    Generic,
    TypeVar,
)
from urllib.parse import parse_qs, quote, urlencode, urlsplit

import httpx

from .errors import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext
from .model import parse_response, to_wire

T = TypeVar("T")

FileInput = bytes | tuple[str, bytes]
"""A file to upload: its content, or its name and content."""

_REDACTED = "***"
_PAGE_MARKERS = ("page", "cursor")


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


def _read(settings: Settings, method: str, response: httpx.Response) -> Any:
    text = response.text
    _log(settings, logging.DEBUG, f"<- {method} {response.status_code} ({len(text)} chars)")
    if not response.is_success:
        clean = text.replace(settings.secret, _REDACTED)
        raise settings.to_error(ErrorContext(response.status_code, response.headers, clean, _parse_json(clean)))
    if text == "":
        return None
    if "json" not in response.headers.get("content-type", ""):
        return text
    try:
        return json.loads(text)
    except ValueError:
        raise DecodeError("The response body is not valid JSON", status=response.status_code) from None


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
    except (TypeError, ValueError):
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
        return settings.rate_limit_wait if wait is None else wait
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
    position = parse_qs(urlsplit(str(link)).query)
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

    # TODO: httpx applies the timeout per network operation, so a body that keeps trickling can
    # outlast it. Enforce one deadline per attempt.
    def fetch(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> Any:
        settings = self.settings
        request = _build_request(settings, operation, body, params)
        tries = 0
        while True:
            _log(settings, logging.DEBUG, f"-> {request['method']} {request['url']}")
            try:
                try:
                    response = self.http.request(**request)
                except httpx.TransportError as error:
                    raise _translate(error) from error
                return _read(settings, operation.method, response)
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

    async def fetch(self, operation: Operation[Any], body: Any, params: Mapping[str, Any]) -> Any:
        settings = self.settings
        request = _build_request(settings, operation, body, params)
        tries = 0
        while True:
            _log(settings, logging.DEBUG, f"-> {request['method']} {request['url']}")
            try:
                try:
                    response = await self.http.request(**request)
                except httpx.TransportError as error:
                    raise _translate(error) from error
                return _read(settings, operation.method, response)
            except ApiError as error:
                delay = _retry_delay(settings, error, operation.method, tries)
                if delay is None:
                    raise
                _log(settings, logging.INFO, f"retrying after {delay}s: {error.kind}")
                await asyncio.sleep(delay)
                tries += 1


def _items(page: Any) -> Sequence[Any]:
    results = page.get("results") if isinstance(page, Mapping) else None
    return results if isinstance(results, list) else []


class Resource:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def _call(self, operation: Operation[T], /, *, _body: Any = None, **params: Any) -> T:
        result: T = parse_response(operation.response, self._transport.fetch(operation, _body, params))
        return result

    def _paginate(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> Iterator[Any]:
        current: dict[str, Any] | None = params
        while current is not None:
            page = self._transport.fetch(operation, _body, current)
            for item in _items(page):
                yield parse_response(operation.item, item)
            current = _next_params(operation, current, page)


class AsyncResource:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def _call(self, operation: Operation[T], /, *, _body: Any = None, **params: Any) -> T:
        result: T = parse_response(operation.response, await self._transport.fetch(operation, _body, params))
        return result

    async def _paginate(self, operation: Operation[Any], /, *, _body: Any = None, **params: Any) -> AsyncIterator[Any]:
        current: dict[str, Any] | None = params
        while current is not None:
            page = await self._transport.fetch(operation, _body, current)
            for item in _items(page):
                yield parse_response(operation.item, item)
            current = _next_params(operation, current, page)
