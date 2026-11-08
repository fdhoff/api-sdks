from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from backmarket_seller._runtime import (
    AsyncResource,
    AsyncTransport,
    AuthRequest,
    Credentials,
    Offset,
    Operation,
    Param,
    Resource,
    Settings,
    SyncTransport,
    select_hosts,
)
from backmarket_seller.errors import to_error

HOSTS = {"main": "http://main.invalid", "files": "http://files.invalid/v1"}
ENVIRONMENTS = {
    "production": HOSTS,
    "sandbox": {"main": "http://main.sandbox.invalid/", "files": "http://files.sandbox.invalid"},
}

LIST_ITEMS: Operation[Any] = Operation(
    id="list-items",
    method="GET",
    path="/items",
    resource="items",
    name="list",
    params=(Param("X-Tenant", "x_tenant", "header"),),
    response=dict[str, Any],
    returns_json=True,
)
LIST_FILES: Operation[Any] = Operation(
    id="list-files",
    method="GET",
    path="/files",
    resource="files",
    name="list",
    params=(Param("offset", "offset", "query"),),
    response=dict[str, Any],
    returns_json=True,
    iterator="iter",
    item=dict[str, Any],
    paging=Offset(),
    host="files",
)
GET_MEDIA: Operation[Any] = Operation(
    id="get-media", method="GET", path="/media", resource="media", name="get", host="media"
)


class Recorder(Credentials):
    def __init__(self) -> None:
        self.seen: list[AuthRequest] = []

    def apply(self, request: AuthRequest) -> None:
        self.seen.append(request)
        request.headers["Authorization"] = "Bearer synthetic"


def resource(
    handler: Callable[[httpx.Request], httpx.Response],
    credentials: Credentials | None = None,
    headers: dict[str, str] | None = None,
    **options: Any,
) -> tuple[Resource, list[httpx.Request]]:
    sent: list[httpx.Request] = []

    def record(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return handler(request)

    settings = Settings(
        base_url="http://default.invalid",
        credentials=credentials or Recorder(),
        headers={"User-Agent": "test", "X-Tenant": "client-wide"} if headers is None else headers,
        to_error=to_error,
        logger=logging.getLogger("hosts-test"),
        hosts=HOSTS,
        **options,
    )
    return Resource(SyncTransport(settings, httpx.MockTransport(record))), sent


def ok(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={})


def test_an_operation_with_a_host_key_goes_to_that_host() -> None:
    client, sent = resource(ok)
    client._call(LIST_FILES)
    client._call(LIST_ITEMS)
    assert [str(request.url) for request in sent] == ["http://files.invalid/v1/files", "http://default.invalid/items"]


def test_an_iterator_reissues_every_page_on_the_operation_host() -> None:
    pages = iter([{"count": 3, "results": [{"id": 1}, {"id": 2}]}, {"count": 3, "results": [{"id": 3}]}])
    client, sent = resource(lambda request: httpx.Response(200, json=next(pages)))
    assert len(list(client._paginate(LIST_FILES))) == 3
    assert [str(request.url) for request in sent] == [
        "http://files.invalid/v1/files",
        "http://files.invalid/v1/files?offset=2",
    ]


def test_an_unknown_host_key_fails_before_credentials_or_sending() -> None:
    credentials = Recorder()
    client, sent = resource(ok, credentials)
    with pytest.raises(ValueError, match="'media'"):
        client._call(GET_MEDIA)
    assert sent == []
    assert credentials.seen == []


def test_select_hosts_picks_an_environment_or_checks_the_callers_map() -> None:
    assert select_hosts(ENVIRONMENTS, "sandbox") == {
        "main": "http://main.sandbox.invalid",
        "files": "http://files.sandbox.invalid",
    }
    custom = {"main": "http://localhost:4010/", "files": "http://localhost:4010"}
    assert select_hosts(ENVIRONMENTS, "production", custom) == {
        "main": "http://localhost:4010",
        "files": "http://localhost:4010",
    }
    with pytest.raises(ValueError, match="expected one of: production, sandbox"):
        select_hosts(ENVIRONMENTS, "staging")
    with pytest.raises(ValueError, match="lacks keys: files"):
        select_hosts(ENVIRONMENTS, "production", {"main": "http://localhost"})
    with pytest.raises(ValueError, match="unknown keys: media"):
        select_hosts(ENVIRONMENTS, "production", {**custom, "media": "http://localhost"})


def test_a_header_default_is_sent_only_where_declared_and_a_call_overrides_it() -> None:
    credentials = Recorder()
    client, sent = resource(ok, credentials, header_defaults={"x-tenant": "acme"})
    client._call(LIST_ITEMS)
    client._call(LIST_ITEMS, x_tenant="other")
    client._call(LIST_FILES)
    assert [request.headers.get_list("x-tenant") for request in sent] == [["acme"], ["other"], ["client-wide"]]
    assert credentials.seen[0].headers["X-Tenant"] == "acme"


def test_header_defaults_that_differ_only_by_case_are_rejected_at_construction() -> None:
    with pytest.raises(ValueError, match="differ only by case: X-Tenant, x-tenant"):
        resource(ok, header_defaults={"x-tenant": "acme", "X-Tenant": "other", "X-Other": "unused"})


def test_a_header_with_no_default_and_no_argument_is_not_sent() -> None:
    client, sent = resource(ok, headers={}, header_defaults={"x-other": "unused"})
    client._call(LIST_ITEMS)
    assert "x-tenant" not in sent[0].headers
    assert "x-other" not in sent[0].headers


def test_the_asynchronous_client_routes_and_defaults_the_same_way() -> None:
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(200, json={})

    settings = Settings(
        base_url="http://default.invalid",
        credentials=Recorder(),
        headers={},
        to_error=to_error,
        logger=logging.getLogger("hosts-test"),
        hosts=HOSTS,
        header_defaults={"X-TENANT": "acme"},
    )
    client = AsyncResource(AsyncTransport(settings, httpx.MockTransport(handler)))

    async def run() -> None:
        await client._call(LIST_FILES)
        await client._call(LIST_ITEMS)
        with pytest.raises(ValueError):
            await client._call(GET_MEDIA)

    asyncio.run(run())
    assert [str(request.url) for request in sent] == ["http://files.invalid/v1/files", "http://default.invalid/items"]
    assert sent[1].headers["x-tenant"] == "acme"
    assert "x-tenant" not in sent[0].headers
