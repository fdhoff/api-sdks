from __future__ import annotations

import asyncio
import logging
import threading
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from backmarket_seller import ApiError
from backmarket_seller._runtime import (
    AsyncResource,
    AsyncTransport,
    AuthRequest,
    Credentials,
    Operation,
    Param,
    Resource,
    Scheme,
    Settings,
    StaticCredentials,
    SyncTransport,
)
from backmarket_seller.errors import to_error

KEY = "synthetic-key"
SHARED = "synthetic-shared-secret"
Handler = Callable[[httpx.Request], httpx.Response]

GET_ITEM: Operation[Any] = Operation(
    id="get-item",
    method="GET",
    path="/items/{id}",
    resource="items",
    name="get",
    params=(Param("id", "id", "path"),),
    response=dict[str, Any],
    returns_json=True,
    security=((Scheme("key"), Scheme("user", ("items_r",))),),
)

UPLOAD: Operation[Any] = Operation(
    id="upload",
    method="POST",
    path="/files",
    resource="files",
    name="upload",
    params=(Param("file", "file", "form"),),
    response=dict[str, Any],
    security=((Scheme("key"),),),
)


class Tokens(Credentials):
    """A synthetic bearer token that changes on each refresh, beside a fixed key."""

    def __init__(self) -> None:
        self.version = 1
        self.refreshes = 0
        self.seen: list[AuthRequest] = []

    @property
    def token(self) -> str:
        return f"synthetic-access-{self.version}"

    def apply(self, request: AuthRequest) -> None:
        self.seen.append(request)
        request.headers["x-api-key"] = f"{KEY}:{SHARED}"
        if any(scheme.name == "user" for requirement in request.operation.security for scheme in requirement):
            request.headers["Authorization"] = f"Bearer {self.token}"

    def secrets(self) -> list[str]:
        return [KEY, SHARED, self.token, "synthetic-refresh"]

    def refresh(self, request: AuthRequest) -> bool:
        self.refreshes += 1
        self.version += 1
        return True


class AsyncTokens(Tokens):
    async def refresh(self, request: AuthRequest) -> bool:  # type: ignore[override]
        self.refreshes += 1
        await asyncio.sleep(0.01)
        self.version += 1
        return True


def settings(credentials: Credentials, **options: Any) -> Settings:
    return Settings(
        base_url="http://mock.invalid",
        credentials=credentials,
        headers={"User-Agent": "test"},
        to_error=to_error,
        logger=logging.getLogger("credentials-test"),
        **{"retry_base_delay": 0.0, **options},
    )


def sync_resource(credentials: Credentials, handler: Handler, **options: Any) -> Resource:
    return Resource(SyncTransport(settings(credentials, **options), httpx.MockTransport(handler)))


def async_resource(credentials: Credentials, handler: Handler) -> AsyncResource:
    return AsyncResource(AsyncTransport(settings(credentials), httpx.MockTransport(handler)))


def accepts(token: str) -> Handler:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.headers.get("authorization") != f"Bearer {token}":
            return httpx.Response(401, json={"error": "expired"})
        return httpx.Response(200, json={"id": 1})

    return handler


def test_apply_sees_the_final_request_on_every_attempt() -> None:
    credentials = Tokens()
    replies = iter([httpx.Response(503), httpx.Response(200, json={"id": 1})])
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return next(replies)

    assert sync_resource(credentials, handler)._call(GET_ITEM, id="a b") == {"id": 1}
    assert len(credentials.seen) == 2
    first = credentials.seen[0]
    assert (first.method, first.url, first.body) == ("GET", "http://mock.invalid/items/a%20b", b"")
    assert first.headers["user-agent"] == "test"
    assert first.operation is GET_ITEM
    assert all(request.headers["authorization"] == "Bearer synthetic-access-1" for request in sent)
    assert all(request.headers["x-api-key"] == f"{KEY}:{SHARED}" for request in sent)


def test_apply_gets_the_multipart_bytes_that_are_sent() -> None:
    credentials = Tokens()
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(200, json={})

    sync_resource(credentials, handler)._call(UPLOAD, file=("a.txt", b"hello"))
    seen = credentials.seen[0]
    assert seen.body == sent[0].content
    assert b"hello" in seen.body
    assert seen.headers["content-type"] == sent[0].headers["content-type"]
    assert "authorization" not in sent[0].headers


def test_a_401_refreshes_once_and_retries_once() -> None:
    credentials = Tokens()
    assert sync_resource(credentials, accepts("synthetic-access-2"))._call(GET_ITEM, id="1") == {"id": 1}
    assert credentials.refreshes == 1

    stale = Tokens()
    with pytest.raises(ApiError) as raised:
        sync_resource(stale, accepts("never"))._call(GET_ITEM, id="1")
    assert raised.value.status == 401
    assert stale.refreshes == 1
    assert len(stale.seen) == 2


def test_a_401_is_final_when_the_credentials_cannot_refresh() -> None:
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(401)

    static = StaticCredentials({"Authorization": "Basic synthetic"}, secrets=["synthetic"])
    with pytest.raises(ApiError):
        sync_resource(static, handler)._call(GET_ITEM, id="1")
    assert len(sent) == 1


def test_concurrent_sync_calls_share_one_refresh() -> None:
    credentials = Tokens()
    resource = sync_resource(credentials, accepts("synthetic-access-2"))
    barrier = threading.Barrier(4)
    results: list[Any] = []

    def call() -> None:
        barrier.wait()
        results.append(resource._call(GET_ITEM, id="1"))

    threads = [threading.Thread(target=call) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert results == [{"id": 1}] * 4
    assert credentials.refreshes == 1


def test_concurrent_async_calls_share_one_refresh() -> None:
    async def run() -> list[Any]:
        resource = async_resource(credentials, accepts("synthetic-access-2"))
        return list(await asyncio.gather(*(resource._call(GET_ITEM, id="1") for _ in range(4))))

    credentials = AsyncTokens()
    assert asyncio.run(run()) == [{"id": 1}] * 4
    assert credentials.refreshes == 1


def test_every_secret_is_kept_out_of_errors_and_logs(caplog: pytest.LogCaptureFixture) -> None:
    credentials = Tokens()
    body = f"bad {KEY}:{SHARED} and synthetic-access-1 and synthetic-refresh"

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, text=body)

    caplog.set_level(logging.DEBUG, logger="credentials-test")
    with pytest.raises(ApiError) as raised:
        sync_resource(credentials, handler)._call(GET_ITEM, id=SHARED)
    output = f"{raised.value} {raised.value.raw_body} {caplog.text}"
    for secret in credentials.secrets():
        assert secret not in output
    assert raised.value.raw_body == "bad ***:*** and *** and ***"


def test_the_sync_client_refuses_coroutine_credentials() -> None:
    class Async(Credentials):
        async def apply(self, request: AuthRequest) -> None:
            return None

    with pytest.raises(TypeError, match="asynchronous"):
        sync_resource(Async(), lambda request: httpx.Response(200, json={}))._call(GET_ITEM, id="1")
