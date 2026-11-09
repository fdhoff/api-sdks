from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable
from typing import Any

import httpx

from backmarket_seller._runtime import (
    AsyncResource,
    AsyncTransport,
    AuthRequest,
    Credentials,
    Cursor,
    Operation,
    Param,
    Resource,
    Settings,
    SyncTransport,
)
from backmarket_seller.errors import to_error

GET_ITEM: Operation[Any] = Operation(
    id="get-item",
    method="GET",
    path="/items/{id}",
    resource="items",
    name="get",
    params=(Param("id", "id", "path"), Param("site", "site", "query", defaulted=True)),
    response=dict[str, Any],
    returns_json=True,
)
LIST_ITEMS: Operation[Any] = Operation(
    id="list-items",
    method="GET",
    path="/items",
    resource="items",
    name="list",
    params=(Param("site", "site", "query", defaulted=True), Param("after", "after", "query")),
    response=dict[str, Any],
    returns_json=True,
    iterator="iter",
    item=dict[str, Any],
    paging=Cursor(items="results", next="next", param="after"),
)
LIST_FILES: Operation[Any] = Operation(
    id="list-files",
    method="GET",
    path="/files",
    resource="files",
    name="list",
    params=(Param("site", "site", "query"),),
    response=dict[str, Any],
    returns_json=True,
)


class Recorder(Credentials):
    def apply(self, request: AuthRequest) -> None:
        request.headers["Authorization"] = "Bearer synthetic"


def ok(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={})


def resource(
    handler: Callable[[httpx.Request], httpx.Response], query_defaults: dict[str, str]
) -> tuple[Resource, list[httpx.Request]]:
    sent: list[httpx.Request] = []

    def record(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return handler(request)

    settings = Settings(
        base_url="http://default.invalid",
        credentials=Recorder(),
        headers={},
        to_error=to_error,
        logger=logging.getLogger("query-defaults-test"),
        query_defaults=query_defaults,
    )
    return Resource(SyncTransport(settings, httpx.MockTransport(record))), sent


def test_a_query_default_is_sent_unless_the_call_gives_a_value() -> None:
    client, sent = resource(ok, {"site": "north"})
    client._call(GET_ITEM, id="1")
    client._call(GET_ITEM, id="1", site="south")
    assert [str(request.url) for request in sent] == [
        "http://default.invalid/items/1?site=north",
        "http://default.invalid/items/1?site=south",
    ]


def test_a_query_parameter_with_no_default_and_no_argument_is_not_sent() -> None:
    client, sent = resource(ok, {})
    client._call(GET_ITEM, id="1")
    assert str(sent[0].url) == "http://default.invalid/items/1"


def test_query_default_names_match_exactly() -> None:
    client, sent = resource(ok, {"Site": "north"})
    client._call(GET_ITEM, id="1")
    assert str(sent[0].url) == "http://default.invalid/items/1"


def test_a_query_default_never_reaches_a_parameter_that_does_not_take_one() -> None:
    client, sent = resource(ok, {"site": "north"})
    client._call(LIST_FILES)
    assert str(sent[0].url) == "http://default.invalid/files"


def test_an_iterator_sends_the_query_default_on_every_page() -> None:
    pages = iter([{"results": [{"id": 1}], "next": "b"}, {"results": [{"id": 2}], "next": None}])
    client, sent = resource(lambda request: httpx.Response(200, json=next(pages)), {"site": "north"})
    assert len(list(client._paginate(LIST_ITEMS))) == 2
    assert [str(request.url) for request in sent] == [
        "http://default.invalid/items?site=north",
        "http://default.invalid/items?site=north&after=b",
    ]


def test_the_asynchronous_client_applies_query_defaults_the_same_way() -> None:
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(200, json={})

    settings = Settings(
        base_url="http://default.invalid",
        credentials=Recorder(),
        headers={},
        to_error=to_error,
        logger=logging.getLogger("query-defaults-test"),
        query_defaults={"site": "north"},
    )
    client = AsyncResource(AsyncTransport(settings, httpx.MockTransport(handler)))

    async def run() -> None:
        await client._call(GET_ITEM, id="1")
        await client._call(GET_ITEM, id="1", site="south")

    asyncio.run(run())
    assert [request.url.params.get("site") for request in sent] == ["north", "south"]
