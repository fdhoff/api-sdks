from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from backmarket_seller._runtime import (
    ApiConnectionError,
    AsyncResource,
    AsyncTransport,
    AuthRequest,
    Credentials,
    Operation,
    Resource,
    Settings,
    SyncTransport,
)
from backmarket_seller.errors import ServerError, to_error

TRANSFER: Operation[Any] = Operation(
    id="create-transfer",
    method="POST",
    path="/transfers",
    resource="transfers",
    name="create",
    response=dict[str, Any],
    returns_json=True,
    idempotency_key="idempotency_key",
)
ITEM: Operation[Any] = Operation(
    id="create-item",
    method="POST",
    path="/items",
    resource="items",
    name="create",
    response=dict[str, Any],
    returns_json=True,
)


class Anonymous(Credentials):
    def apply(self, request: AuthRequest) -> None:
        pass

    def secrets(self) -> list[str]:
        return []


def settings() -> Settings:
    return Settings(
        base_url="http://api.invalid",
        credentials=Anonymous(),
        headers={},
        to_error=to_error,
        logger=logging.getLogger("idempotency-test"),
        max_retries=2,
        retry_base_delay=0,
        rate_limit_wait=0,
    )


def recorder(replies: list[httpx.Response]) -> tuple[Callable[[httpx.Request], httpx.Response], list[bytes]]:
    sent: list[bytes] = []
    queue = iter(replies)

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request.read())
        return next(queue)

    return handler, sent


def call(operation: Operation[Any], body: dict[str, Any], replies: list[httpx.Response]) -> tuple[Any, list[bytes]]:
    handler, sent = recorder(replies)
    client = Resource(SyncTransport(settings(), httpx.MockTransport(handler)))
    try:
        return client._call(operation, _body=body), sent
    except ServerError as error:
        return error, sent


def test_a_keyed_write_is_retried_on_a_server_error_with_the_same_body() -> None:
    body = {"idempotency_key": "k-1", "amount": 5}
    result, sent = call(TRANSFER, body, [httpx.Response(503), httpx.Response(200, json={"id": "t-1"})])
    assert result == {"id": "t-1"}
    assert len(sent) == 2
    assert sent[0] == sent[1]
    assert json.loads(sent[0]) == body


def test_a_keyed_write_is_retried_after_a_dropped_connection() -> None:
    sent: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request.read())
        if len(sent) == 1:
            raise httpx.ConnectError("dropped", request=request)
        return httpx.Response(200, json={"id": "t-2"})

    client = Resource(SyncTransport(settings(), httpx.MockTransport(handler)))
    assert client._call(TRANSFER, _body={"idempotency_key": "k-2"}) == {"id": "t-2"}
    assert sent[0] == sent[1]


@pytest.mark.parametrize(
    ("operation", "body"),
    [
        (ITEM, {"idempotency_key": "k-3", "name": "widget"}),
        (TRANSFER, {"idempotency_key": "", "amount": 5}),
        (TRANSFER, {"idempotency_key": None, "amount": 5}),
        (TRANSFER, {"amount": 5}),
    ],
)
def test_a_write_without_a_key_is_not_retried_on_a_server_error(
    operation: Operation[Any], body: dict[str, Any]
) -> None:
    result, sent = call(operation, body, [httpx.Response(503), httpx.Response(200, json={})])
    assert isinstance(result, ServerError)
    assert len(sent) == 1


def test_a_write_without_a_key_is_still_retried_on_a_rate_limit() -> None:
    result, sent = call(TRANSFER, {"amount": 5}, [httpx.Response(429), httpx.Response(200, json={"id": "t-3"})])
    assert result == {"id": "t-3"}
    assert len(sent) == 2


def test_the_async_client_retries_a_keyed_write_and_not_an_unkeyed_one() -> None:
    async def run(body: dict[str, Any]) -> list[bytes]:
        sent: list[bytes] = []

        async def handler(request: httpx.Request) -> httpx.Response:
            sent.append(await request.aread())
            if len(sent) == 1:
                raise httpx.ConnectError("dropped", request=request)
            return httpx.Response(200, json={})

        client = AsyncResource(AsyncTransport(settings(), httpx.MockTransport(handler)))
        try:
            await client._call(TRANSFER, _body=body)
        except ApiConnectionError:
            pass
        return sent

    keyed = asyncio.run(run({"idempotency_key": "k-4"}))
    assert len(keyed) == 2 and keyed[0] == keyed[1]
    assert len(asyncio.run(run({"idempotency_key": ""}))) == 1
