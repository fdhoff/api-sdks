"""Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.

The client adds `/api/v1` to the instance URL, while the cases name each path as the spec declares it, because the
mock serves them without the prefix. The driver's transport removes the prefix on the way out. A request without it
goes out unchanged, so its path fails the case's wire check.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import logging
import sys
from collections.abc import AsyncIterator
from typing import Any, get_args, get_type_hints

import httpx

from gitea_rest import ApiError, AsyncDownload, AsyncGiteaClient, Download, GiteaClient, HttpError
from gitea_rest._resources import OPERATIONS
from gitea_rest._runtime import ApiModel, Operation, to_wire
from gitea_rest.client import API_PATH

PREFIX = API_PATH.encode()


def unprefixed(request: httpx.Request) -> None:
    raw_path = request.url.raw_path
    if raw_path.startswith(PREFIX + b"/"):
        request.url = request.url.copy_with(raw_path=raw_path[len(PREFIX) :])


class SyncPrefixTransport(httpx.BaseTransport):
    def __init__(self) -> None:
        self.inner = httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        unprefixed(request)
        return self.inner.handle_request(request)

    def close(self) -> None:
        self.inner.close()


class AsyncPrefixTransport(httpx.AsyncBaseTransport):
    def __init__(self) -> None:
        self.inner = httpx.AsyncHTTPTransport()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        unprefixed(request)
        return await self.inner.handle_async_request(request)

    async def aclose(self) -> None:
        await self.inner.aclose()


class Capture(logging.Handler):
    def __init__(self) -> None:
        super().__init__(logging.DEBUG)
        self.lines: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.lines.append(record.getMessage())


def client_options(settings: dict[str, Any]) -> dict[str, Any]:
    """A case that sets `username` uses Basic, with the one-time password unless it is null. Otherwise the token."""
    options: dict[str, Any] = {"base_url": settings["base_url"]}
    if "username" in settings:
        options.update(username=settings["username"], password=settings["password"], otp=settings.get("otp"))
    else:
        options["token"] = settings["token"]
    if settings.get("sudo") is not None:
        options["sudo"] = settings["sudo"]
    if "user_agent" in settings:
        options["user_agent"] = settings["user_agent"]
    seconds = {
        "timeout_ms": "timeout",
        "retry_base_delay_ms": "retry_base_delay",
        "rate_limit_wait_ms": "rate_limit_wait",
        "max_retry_wait_ms": "max_retry_wait",
    }
    for key, name in seconds.items():
        if key in settings:
            options[name] = settings[key] / 1000
    if "max_retries" in settings:
        options["max_retries"] = settings["max_retries"]
    return options


def types(hint: Any) -> list[Any]:
    """The types a hint allows, with Optional, unions and lists opened up."""
    args = get_args(hint)
    return [hint] if not args else [found for arg in args for found in types(arg)]


def value_for(hint: Any, value: Any) -> Any:
    """Cases give every parameter as JSON. Files are sent as bytes, a JSON part as its object, and an integer
    parameter given as a string as the integer."""
    allowed = types(hint)
    if isinstance(value, list):
        return [value_for(hint, item) for item in value]
    if not isinstance(value, str):
        return value
    if bytes in allowed:
        return value.encode()
    if any(isinstance(kind, type) and issubclass(kind, ApiModel) for kind in allowed):
        return json.loads(value)
    if int in allowed and str not in allowed:
        return int(value)
    return value


def arguments(operation: Operation[Any], request: dict[str, Any], call: Any) -> dict[str, Any]:
    """A form body's fields are method arguments, like path and query parameters."""
    names = {param.wire: param.name for param in operation.params}
    hints = get_type_hints(call)
    values = {**request.get("params", {}), **request.get("multipart", {})}
    args = {names[wire]: value_for(hints.get(names[wire]), value) for wire, value in values.items()}
    if "body" in request:
        args["body"] = request["body"]
    return args


def target(client: Any, operation: Operation[Any], request: dict[str, Any]) -> Any:
    if request.get("paginate"):
        assert operation.iterator is not None, f"{operation.id} has no iterator"
        name = operation.iterator
    else:
        name = operation.name
    return getattr(getattr(client, operation.resource), name)


def error_output(error: ApiError) -> dict[str, Any]:
    message = error.message if isinstance(error, HttpError) else None
    fields = {"kind": error.kind, "status": error.status, "message": message, "raw_body": error.raw_body}
    return {name: value for name, value in fields.items() if value is not None}


def download_output(content_type: str, body: bytes) -> dict[str, str]:
    return {"content_type": content_type, "base64": base64.b64encode(body).decode()}


def run_sync(message: dict[str, Any]) -> Any:
    request = message["request"]
    with GiteaClient(**client_options(message["client"]), http_transport=SyncPrefixTransport()) as client:
        operation = OPERATIONS[request["operation"]]
        call = target(client, operation, request)
        result = call(**arguments(operation, request, call))
        if isinstance(result, Download):
            with result:
                return download_output(result.content_type, result.read())
        return list(result) if request.get("paginate") else result


async def collect(items: AsyncIterator[Any]) -> list[Any]:
    return [item async for item in items]


async def run_async(message: dict[str, Any]) -> Any:
    request = message["request"]
    async with AsyncGiteaClient(**client_options(message["client"]), http_transport=AsyncPrefixTransport()) as client:
        operation = OPERATIONS[request["operation"]]
        call = target(client, operation, request)
        args = arguments(operation, request, call)
        if request.get("paginate"):
            return await collect(call(**args))
        result = await call(**args)
        if isinstance(result, AsyncDownload):
            async with result:
                return download_output(result.content_type, await result.aread())
        return result


def output(message: dict[str, Any], capture: Capture, loop: asyncio.AbstractEventLoop | None) -> dict[str, Any]:
    capture.lines = []
    try:
        result = loop.run_until_complete(run_async(message)) if loop else run_sync(message)
    except ApiError as error:
        return {"error": error_output(error), "logs": capture.lines}
    return {"result": to_wire(result), "logs": capture.lines}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["sync", "async"], default="sync")
    mode = parser.parse_args().mode

    capture = Capture()
    logger = logging.getLogger("gitea_rest")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(capture)
    logger.propagate = False

    loop = asyncio.new_event_loop() if mode == "async" else None
    for line in sys.stdin:
        reply = output(json.loads(line), capture, loop)
        print(json.dumps(reply), flush=True)


if __name__ == "__main__":
    main()
