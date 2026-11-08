"""Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README."""

from __future__ import annotations

import argparse
import asyncio
import importlib
import json
import logging
import sys
from collections.abc import AsyncIterator
from typing import Any
from urllib.parse import urlsplit

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

from ebay_sell import ApiError, AsyncEbayClient, EbayClient, HttpError, SigningKey
from ebay_sell._runtime import Operation, to_wire
from ebay_sell.client import ENVIRONMENTS

# Each contract's name in the cases, and the client attribute that holds it.
CONTRACTS = {
    "sell_account_v1": "account",
    "sell_account_v2": "account_v2",
    "sell_analytics": "analytics",
    "sell_feed": "feed",
    "sell_finances": "finances",
    "sell_fulfillment": "fulfillment",
    "sell_inventory": "inventory",
    "sell_marketing": "marketing",
    "sell_metadata": "metadata",
    "sell_negotiation": "negotiation",
    "sell_recommendation": "recommendation",
    "sell_stores": "stores",
    "commerce_feedback": "feedback",
    "commerce_identity": "identity",
    "commerce_media": "media",
    "commerce_message": "message",
    "commerce_notification": "notification",
    "commerce_taxonomy": "taxonomy",
    "developer_analytics": "developer_analytics",
    "developer_key_management": "key_management",
}
OPERATIONS: dict[str, tuple[str, Operation[Any]]] = {
    f"{contract}.{operation.id}": (module, operation)
    for contract, module in CONTRACTS.items()
    for operation in importlib.import_module(f"ebay_sell.{module}._resources").OPERATIONS.values()
}
FORM = ("form", "urlencoded")
# Generated per run, never stored: the cases check the signature's shape and digest, not the key.
PRIVATE_KEY = (
    ed25519.Ed25519PrivateKey.generate()
    .private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
    .decode()
)


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
    options: dict[str, Any] = {
        "app_token": settings["app_token"],
        "user_token": settings["user_token"],
        "hosts": hosts(settings),
    }
    if "environment" in settings:
        options["environment"] = settings["environment"]
    defaults = settings.get("header_defaults", {})
    options["marketplace_id"] = defaults.get("X-EBAY-C-MARKETPLACE-ID")
    options["content_language"] = defaults.get("Content-Language")
    if "signature_key" in settings:
        options["signing_key"] = SigningKey(PRIVATE_KEY, settings["signature_key"])
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


def arguments(operation: Operation[Any], request: dict[str, Any]) -> dict[str, Any]:
    """A form body's fields are method arguments, like path, query and header parameters."""
    names = {param.wire: param.name for param in operation.params}
    values = {**request.get("params", {}), **request.get("multipart", {})}
    form = any(param.location in FORM for param in operation.params)
    if form:
        values.update(request.get("body", {}))
    args = {names[wire]: value.encode() if names[wire] == "file" else value for wire, value in values.items()}
    if "body" in request and not form:
        args["body"] = request["body"]
    return args


def target(client: Any, module: str, operation: Operation[Any], paginate: bool) -> Any:
    name = operation.iterator if paginate else operation.name
    assert name is not None, f"{operation.id} has no iterator"
    return getattr(getattr(getattr(client, module), operation.resource), name)


def error_output(error: ApiError) -> dict[str, Any]:
    fields = {
        "kind": error.kind,
        "status": error.status,
        "raw_body": error.raw_body,
        "message": error.message if isinstance(error, HttpError) else None,
        "code": error.code,
    }
    return {name: value for name, value in fields.items() if value is not None}


def run_sync(message: dict[str, Any]) -> Any:
    request = message["request"]
    module, operation = OPERATIONS[request["operation"]]
    with EbayClient(**client_options(message["client"])) as client:
        call = target(client, module, operation, bool(request.get("paginate")))
        result = call(**arguments(operation, request))
        return list(result) if request.get("paginate") else result


async def collect(items: AsyncIterator[Any]) -> list[Any]:
    return [item async for item in items]


async def run_async(message: dict[str, Any]) -> Any:
    request = message["request"]
    module, operation = OPERATIONS[request["operation"]]
    async with AsyncEbayClient(**client_options(message["client"])) as client:
        call = target(client, module, operation, bool(request.get("paginate")))
        if request.get("paginate"):
            return await collect(call(**arguments(operation, request)))
        return await call(**arguments(operation, request))


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
    logger = logging.getLogger("ebay_sell")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(capture)
    logger.propagate = False

    loop = asyncio.new_event_loop() if mode == "async" else None
    for line in sys.stdin:
        reply = output(json.loads(line), capture, loop)
        print(json.dumps(reply), flush=True)


if __name__ == "__main__":
    main()
