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
from urllib.parse import urlsplit

from mercury_banking import ENVIRONMENTS, ApiError, AsyncMercuryClient, MercuryClient
from mercury_banking._resources import OPERATIONS
from mercury_banking._runtime import AsyncDownload, Download, Operation, to_wire

FORM = ("form", "urlencoded")


class Capture(logging.Handler):
    def __init__(self) -> None:
        super().__init__(logging.DEBUG)
        self.lines: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.lines.append(record.getMessage())


def hosts(settings: dict[str, Any]) -> dict[str, str]:
    """Each host key's harness prefix: the key itself, or with an environment the hostname it maps the key to."""
    base_url = settings["base_url"]
    if "environment" in settings:
        urls = ENVIRONMENTS[settings["environment"]]
        return {key: f"{base_url}/_host/{urlsplit(url).hostname}" for key, url in urls.items()}
    return {key: f"{base_url}/_host/{key}" for key in ENVIRONMENTS["production"]}


def client_options(settings: dict[str, Any]) -> dict[str, Any]:
    options: dict[str, Any] = {"hosts": hosts(settings)}
    if "environment" in settings:
        options["environment"] = settings["environment"]
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


def takes_file(hint: Any) -> bool:
    return hint is bytes or any(takes_file(arg) for arg in get_args(hint))


def arguments(operation: Operation[Any], request: dict[str, Any], call: Any) -> dict[str, Any]:
    """A form body's fields are method arguments, like path and query parameters. Files are sent as bytes."""
    names = {param.wire: param.name for param in operation.params}
    hints = get_type_hints(call)
    values = {**request.get("params", {}), **request.get("multipart", {})}
    form = any(param.location in FORM for param in operation.params)
    if form:
        values.update(request.get("body", {}))
    args = {
        names[wire]: value.encode() if isinstance(value, str) and takes_file(hints.get(names[wire])) else value
        for wire, value in values.items()
    }
    if "body" in request and not form:
        args["body"] = request["body"]
    return args


def target(client: Any, operation: Operation[Any], paginate: bool) -> Any:
    name = operation.iterator if paginate else operation.name
    assert name is not None, f"{operation.id} has no iterator"
    return getattr(getattr(client, operation.resource), name)


def error_output(error: ApiError) -> dict[str, Any]:
    fields = {"kind": error.kind, "status": error.status, "raw_body": error.raw_body}
    return {name: value for name, value in fields.items() if value is not None}


def download_output(content_type: str, body: bytes) -> dict[str, str]:
    return {"content_type": content_type, "base64": base64.b64encode(body).decode()}


def run_sync(message: dict[str, Any]) -> Any:
    request = message["request"]
    operation = OPERATIONS[request["operation"]]
    settings = message["client"]
    with MercuryClient(settings["token"], **client_options(settings)) as client:
        call = target(client, operation, bool(request.get("paginate")))
        result = call(**arguments(operation, request, call))
        if isinstance(result, Download):
            with result:
                return download_output(result.content_type, result.read())
        return list(result) if request.get("paginate") else result


async def collect(items: AsyncIterator[Any]) -> list[Any]:
    return [item async for item in items]


async def run_async(message: dict[str, Any]) -> Any:
    request = message["request"]
    operation = OPERATIONS[request["operation"]]
    settings = message["client"]
    async with AsyncMercuryClient(settings["token"], **client_options(settings)) as client:
        call = target(client, operation, bool(request.get("paginate")))
        if request.get("paginate"):
            return await collect(call(**arguments(operation, request, call)))
        result = await call(**arguments(operation, request, call))
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
    logger = logging.getLogger("mercury_banking")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(capture)
    logger.propagate = False

    loop = asyncio.new_event_loop() if mode == "async" else None
    for line in sys.stdin:
        reply = output(json.loads(line), capture, loop)
        print(json.dumps(reply), flush=True)


if __name__ == "__main__":
    main()
