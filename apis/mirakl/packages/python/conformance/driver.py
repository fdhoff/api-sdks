"""Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README."""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import logging
import sys
from collections.abc import AsyncIterator
from typing import Any, get_args, get_type_hints

from mirakl_seller import ApiError, AsyncDownload, AsyncMiraklClient, Download, MiraklClient
from mirakl_seller._resources import OPERATIONS
from mirakl_seller._runtime import ApiModel, Operation, to_wire


class Capture(logging.Handler):
    def __init__(self) -> None:
        super().__init__(logging.DEBUG)
        self.lines: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.lines.append(record.getMessage())


def client_options(settings: dict[str, Any]) -> dict[str, Any]:
    options: dict[str, Any] = {"base_url": settings["base_url"]}
    shop_id = settings.get("query_defaults", {}).get("shop_id")
    if shop_id is not None:
        options["shop_id"] = int(shop_id)
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


def wait_options(settings: dict[str, Any]) -> dict[str, float]:
    options = {"poll_interval_ms": "interval", "poll_timeout_ms": "timeout"}
    return {name: settings[key] / 1000 for key, name in options.items() if key in settings}


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
    if request.get("wait"):
        # Each status operation's wait method is named after it: get_import polls through wait_for_import.
        assert operation.job is not None, f"{operation.id} reports no job"
        name = operation.name.replace("get_", "wait_for_", 1)
    elif request.get("paginate"):
        assert operation.iterator is not None, f"{operation.id} has no iterator"
        name = operation.iterator
    else:
        name = operation.name
    return getattr(getattr(client, operation.resource), name)


def error_output(error: ApiError) -> dict[str, Any]:
    fields = {"kind": error.kind, "status": error.status, "raw_body": error.raw_body}
    return {name: value for name, value in fields.items() if value is not None}


def download_output(content_type: str, body: bytes) -> dict[str, str]:
    return {"content_type": content_type, "base64": base64.b64encode(body).decode()}


def run_sync(message: dict[str, Any]) -> Any:
    request = message["request"]
    settings = message["client"]
    with MiraklClient(settings["token"], **client_options(settings)) as client:
        if "download" in request:
            with client.download_url(request["download"]) as download:
                return download_output(download.content_type, download.read())
        operation = OPERATIONS[request["operation"]]
        call = target(client, operation, request)
        args = arguments(operation, request, call)
        result = call(**args, **wait_options(settings)) if request.get("wait") else call(**args)
        if isinstance(result, Download):
            with result:
                return download_output(result.content_type, result.read())
        return list(result) if request.get("paginate") else result


async def collect(items: AsyncIterator[Any]) -> list[Any]:
    return [item async for item in items]


async def run_async(message: dict[str, Any]) -> Any:
    request = message["request"]
    settings = message["client"]
    async with AsyncMiraklClient(settings["token"], **client_options(settings)) as client:
        if "download" in request:
            async with await client.download_url(request["download"]) as download:
                return download_output(download.content_type, await download.aread())
        operation = OPERATIONS[request["operation"]]
        call = target(client, operation, request)
        args = arguments(operation, request, call)
        if request.get("paginate"):
            return await collect(call(**args))
        result = await (call(**args, **wait_options(settings)) if request.get("wait") else call(**args))
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
    logger = logging.getLogger("mirakl_seller")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(capture)
    logger.propagate = False

    loop = asyncio.new_event_loop() if mode == "async" else None
    for line in sys.stdin:
        reply = output(json.loads(line), capture, loop)
        print(json.dumps(reply), flush=True)


if __name__ == "__main__":
    main()
