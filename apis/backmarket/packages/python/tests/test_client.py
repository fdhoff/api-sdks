from __future__ import annotations

import asyncio
import gzip
import logging
import time
from collections.abc import AsyncIterator, Callable, Iterator
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from typing import Any, cast

import httpx
import pytest
from pydantic import Field, ValidationError

from backmarket_seller import (
    ApiConnectionError,
    ApiError,
    ApiTimeoutError,
    AsyncBackMarketClient,
    BackMarketClient,
    DecodeError,
    Environment,
    RateLimitedError,
    Region,
    ServerError,
    WafBlockedError,
)
from backmarket_seller._resources import OPERATIONS
from backmarket_seller._runtime.model import ApiModel, parse_response
from backmarket_seller._runtime.transport import _retry_after
from backmarket_seller.models import CategoryTree, Order, OrderPage, UpdateOrder

TOKEN = "synthetic-token"
Handler = Callable[[httpx.Request], httpx.Response]


def client_for(handler: Handler, **options: Any) -> BackMarketClient:
    defaults: dict[str, Any] = {"user_agent": "BM-Example-Test;test@example.com", "locale": "en-us"}
    return BackMarketClient(
        TOKEN,
        base_url="http://mock.invalid",
        http_transport=httpx.MockTransport(handler),
        **{**defaults, **options},
    )


def test_every_operation_has_a_public_method() -> None:
    client = client_for(lambda request: httpx.Response(200))
    assert len(OPERATIONS) == 40
    for operation in OPERATIONS.values():
        resource = getattr(client, operation.resource)
        assert callable(getattr(resource, operation.name))
        if operation.iterator:
            assert callable(getattr(resource, operation.iterator))


@pytest.mark.parametrize(
    ("region", "environment", "host"),
    [
        (Region.EU, Environment.PRODUCTION, "www.backmarket.fr"),
        (Region.NA, Environment.PREPROD, "preprod.backmarket.com"),
        (Region.AP, Environment.PRODUCTION, "www.backmarket.co.jp"),
    ],
)
def test_region_and_environment_select_the_server(region: Region, environment: Environment, host: str) -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.url.host)
        return httpx.Response(200, json={"order_id": 1})

    client = BackMarketClient(
        TOKEN,
        user_agent="agent",
        locale="en-us",
        region=region,
        environment=environment,
        http_transport=httpx.MockTransport(handler),
    )
    client.orders.get(1)
    assert seen == [host]


def test_server_choice_is_required_and_exclusive() -> None:
    with pytest.raises(ValueError):
        BackMarketClient(TOKEN, user_agent="agent", locale="en-us")
    with pytest.raises(ValueError):
        BackMarketClient(TOKEN, user_agent="agent", locale="en-us", region=Region.EU, base_url="http://mock.invalid")


def test_user_agent_is_required() -> None:
    with pytest.raises(ValueError):
        BackMarketClient(TOKEN, user_agent="", locale="en-us", region=Region.EU)


def test_responses_tolerate_what_the_spec_got_wrong() -> None:
    client = client_for(lambda request: httpx.Response(200, json={"order_id": "not-an-int", "surprise": 1}))
    order: Any = client.orders.get(1)
    assert type(order).__name__ == "Order"
    assert order.to_wire() == {"order_id": "not-an-int", "surprise": 1}


def test_nested_models_survive_a_bad_sibling() -> None:
    tree = {
        "category_id": "wrong",
        "childrens": [
            {
                "category_id": 2,
                "category_name": "x",
                "marketplace_category_id": 3,
                "is_leaf": True,
                "attributes": [],
                "childrens": [],
            }
        ],
    }
    client = client_for(lambda request: httpx.Response(200, json=tree))
    branch = client.categories.get(1)
    assert isinstance(branch, CategoryTree)
    assert isinstance(branch.childrens[0], CategoryTree)
    assert branch.childrens[0].category_id == 2


class Place(ApiModel):
    postal_code: str = Field(alias="postalCode")
    city: str


def test_salvage_keeps_a_field_sent_under_both_names() -> None:
    place: Any = parse_response(Place, {"postalCode": "00000", "postal_code": "other", "city": 1})
    assert place.postal_code == "00000"
    assert place.city == 1
    assert place.to_wire() == {"postalCode": "00000", "postal_code": "other", "city": 1}


@pytest.mark.parametrize("key", ["_fields_set", "cls"])
def test_salvage_keeps_unknown_keys_named_like_its_own_arguments(key: str) -> None:
    place: Any = parse_response(Place, {"postalCode": 1, key: "kept"})
    assert place.model_extra == {key: "kept"}


def test_a_response_that_is_not_an_object_is_a_decode_error() -> None:
    client = client_for(lambda request: httpx.Response(200, json=["unexpected", TOKEN]))
    with pytest.raises(DecodeError) as caught:
        client.orders.get(1)
    assert caught.value.raw_body == '["unexpected", "***"]'


def test_an_empty_body_for_a_typed_response_is_a_decode_error() -> None:
    client = client_for(lambda request: httpx.Response(200))
    with pytest.raises(DecodeError) as caught:
        client.orders.get(1)
    assert caught.value.raw_body is None


def test_an_iterated_item_that_is_not_an_object_is_a_decode_error() -> None:
    page = {"next": None, "results": [{"order_id": 1}, "unexpected"]}
    client = client_for(lambda request: httpx.Response(200, json=page))
    with pytest.raises(DecodeError):
        list(client.orders.iter())


def test_an_operation_with_no_declared_response_returns_none() -> None:
    client = client_for(lambda request: httpx.Response(200, json={"unexpected": 1}))
    assert client.orders.upload_invoice(1, invoice=[b"%PDF"]) is None


def test_parameter_constraints_are_enforced_before_sending() -> None:
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(200, json={"results": []})

    client = client_for(handler)
    with pytest.raises(ValidationError, match="page_size"):
        client.orders.list(page_size=500)
    with pytest.raises(ValidationError, match="page_size"):
        client.orders.iter(page_size=51)
    with pytest.raises(ValidationError, match="order_id"):
        client.orders.get(cast(Any, "1"))
    assert sent == []

    client.orders.list(page_size=50)
    assert [request.url.query for request in sent] == [b"page-size=50"]


def test_parameters_are_checked_but_sent_as_given() -> None:
    queries: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        queries.append(request.url.query)
        return httpx.Response(200, json={"results": []})

    client_for(handler).orders.list(date_creation=cast(Any, "2026-01-02"))
    assert queries == [b"date_creation=2026-01-02"]


def test_async_parameter_constraints_are_enforced_before_sending() -> None:
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(200, json={"results": []})

    async def run() -> None:
        async with AsyncBackMarketClient(
            TOKEN,
            user_agent="agent",
            locale="en-us",
            base_url="http://mock.invalid",
            http_transport=httpx.MockTransport(handler),
        ) as client:
            with pytest.raises(ValidationError, match="page_size"):
                await client.orders.list(page_size=500)
            with pytest.raises(ValidationError, match="page_size"):
                client.orders.iter(page_size=500)

    asyncio.run(run())
    assert sent == []


@pytest.mark.parametrize("headers", [{"content-type": "application/json"}, {}])
def test_an_empty_success_body_is_a_decode_error(headers: dict[str, str]) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers=headers)

    with pytest.raises(DecodeError) as caught:
        client_for(handler).orders.get(1)
    assert caught.value.status == 200
    with pytest.raises(DecodeError):
        async_order(handler)


def test_an_empty_body_is_fine_where_none_is_declared() -> None:
    client = client_for(lambda request: httpx.Response(201))
    client.care.transfer_item(1, {})
    assert client.care.create_refund({}) == ""


def test_request_models_are_strict() -> None:
    with pytest.raises(ValidationError):
        UpdateOrder.model_validate({"order_id": "not-an-int", "new_state": 1})


def test_request_models_send_only_what_was_set_under_wire_names() -> None:
    bodies: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(request.content)
        return httpx.Response(200, json={"order_id": 1})

    client_for(handler).orders.update(1, UpdateOrder.model_validate({"order_id": 1, "new_state": 1}))
    assert bodies == [b'{"order_id":1,"new_state":1}']


def test_page_model_is_returned_by_list() -> None:
    page = {"count": 1, "next": None, "previous": None, "results": [{"order_id": 1}]}
    client = client_for(lambda request: httpx.Response(200, json=page))
    assert isinstance(client.orders.list(), OrderPage)


def test_iterator_rejects_a_next_link_that_does_not_advance() -> None:
    page = {"next": "https://foreign.invalid/ws/orders?page=1", "results": [{"order_id": 1}]}
    client = client_for(lambda request: httpx.Response(200, json=page))
    with pytest.raises(DecodeError):
        list(client.orders.iter(page=1))


def test_iterator_rejects_a_next_link_with_no_position() -> None:
    page = {"next": "https://foreign.invalid/ws/orders", "results": []}
    client = client_for(lambda request: httpx.Response(200, json=page))
    with pytest.raises(DecodeError):
        list(client.orders.iter())


def test_iterator_rejects_a_next_link_that_is_not_a_url() -> None:
    page = {"next": "http://[", "results": [{"order_id": 1}]}
    client = client_for(lambda request: httpx.Response(200, json=page))
    with pytest.raises(DecodeError):
        list(client.orders.iter())


def test_redirects_are_not_followed() -> None:
    hosts: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        hosts.append(request.url.host)
        return httpx.Response(302, headers={"location": "https://foreign.invalid/"})

    with pytest.raises(ApiError) as caught:
        client_for(handler).orders.get(1)
    assert caught.value.status == 302
    assert hosts == ["mock.invalid"]


def test_waf_error_is_a_permission_error_and_keeps_cf_ray() -> None:
    response = httpx.Response(403, headers={"cf-ray": "ray-1"}, text="<html></html>")
    with pytest.raises(WafBlockedError) as caught:
        client_for(lambda request: response).orders.get(1)
    assert caught.value.cf_ray == "ray-1"


def test_connection_failure_on_get_is_retried_then_raised() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.method)
        raise httpx.ConnectError("refused", request=request)

    with pytest.raises(ApiConnectionError):
        client_for(handler, max_retries=2, retry_base_delay=0).orders.get(1)
    assert calls == ["GET", "GET", "GET"]


def test_token_is_not_logged(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG, logger="backmarket_seller")

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, text=f"bad {TOKEN}")

    with pytest.raises(ApiError) as caught:
        client_for(handler).orders.get(1)
    assert caplog.records
    assert TOKEN not in caplog.text
    assert TOKEN not in str(caught.value)
    assert TOKEN not in (caught.value.raw_body or "")


class SlowBody(httpx.SyncByteStream, httpx.AsyncByteStream):
    def __init__(self, *chunks: bytes, pause: float = 0.0) -> None:
        self.chunks = chunks
        self.pause = pause

    def __iter__(self) -> Iterator[bytes]:
        for chunk in self.chunks:
            time.sleep(self.pause)
            yield chunk

    async def __aiter__(self) -> AsyncIterator[bytes]:
        for chunk in self.chunks:
            await asyncio.sleep(self.pause)
            yield chunk


def corrupt(status: int, **headers: str) -> Handler:
    headers = {"content-encoding": "gzip", "content-type": "application/json", **headers}
    return lambda request: httpx.Response(status, headers=headers, stream=SlowBody(b"not gzip"))


def async_order(handler: Handler, **options: Any) -> Any:
    async def run() -> Any:
        async with AsyncBackMarketClient(
            TOKEN,
            user_agent="agent",
            locale="en-us",
            base_url="http://mock.invalid",
            http_transport=httpx.MockTransport(handler),
            **options,
        ) as client:
            return await client.orders.get(1)

    return asyncio.run(run())


def test_corrupt_compressed_success_is_a_decode_error() -> None:
    with pytest.raises(DecodeError) as caught:
        client_for(corrupt(200)).orders.get(1)
    assert caught.value.status == 200


def test_corrupt_compressed_success_is_a_decode_error_in_async() -> None:
    with pytest.raises(DecodeError):
        async_order(corrupt(200))


def gzipped(body: bytes, status: int = 200) -> Handler:
    headers = {"content-encoding": "gzip", "content-type": "application/json"}
    return lambda request: httpx.Response(status, headers=headers, stream=SlowBody(body))


ORDER_GZIP = gzip.compress(b'{"order_id": 1, "delivery_note": "synthetic"}')


@pytest.mark.parametrize("body", [ORDER_GZIP[:10], ORDER_GZIP[: len(ORDER_GZIP) // 2], ORDER_GZIP[:-8]])
def test_truncated_compressed_success_is_a_decode_error(body: bytes) -> None:
    with pytest.raises(DecodeError) as caught:
        client_for(gzipped(body)).orders.get(1)
    assert caught.value.status == 200
    with pytest.raises(DecodeError):
        async_order(gzipped(body))


def test_compressed_success_reads_every_member() -> None:
    body = gzip.compress(b'{"order_id": 1, ') + gzip.compress(b'"delivery_note": "synthetic"}')
    for order in (client_for(gzipped(body)).orders.get(1), async_order(gzipped(body))):
        assert order.order_id == 1
        assert order.delivery_note == "synthetic"


def test_truncated_compressed_failure_keeps_its_status() -> None:
    with pytest.raises(ServerError) as caught:
        client_for(gzipped(ORDER_GZIP[:-8], status=502), max_retries=0).orders.get(1)
    assert caught.value.raw_body == ""


def test_corrupt_compressed_failure_keeps_its_status() -> None:
    with pytest.raises(ServerError) as caught:
        client_for(corrupt(502), max_retries=0).orders.get(1)
    assert caught.value.status == 502
    assert caught.value.raw_body == ""


def test_corrupt_compressed_429_still_honours_retry_after() -> None:
    answers: list[Handler] = [
        corrupt(429, **{"retry-after": "0"}),
        lambda request: httpx.Response(200, json={"order_id": 1}),
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        return answers.pop(0)(request)

    assert client_for(handler, rate_limit_wait=60).orders.get(1).order_id == 1


def trickling(request: httpx.Request) -> httpx.Response:
    headers = {"content-type": "application/json"}
    return httpx.Response(200, headers=headers, stream=SlowBody(b"{", b"}", b" ", b" ", pause=0.02))


def test_a_trickling_body_cannot_outlast_the_timeout() -> None:
    with pytest.raises(ApiTimeoutError):
        client_for(trickling, timeout=0.03, max_retries=0).orders.get(1)


def test_a_trickling_body_cannot_outlast_the_timeout_in_async() -> None:
    with pytest.raises(ApiTimeoutError):
        async_order(trickling, timeout=0.03, max_retries=0)


def test_a_body_that_arrives_in_time_is_read_across_chunks() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, headers={"content-type": "application/json"}, stream=SlowBody(b'{"order_id"', b":1}")
        )

    assert client_for(handler).orders.get(1).order_id == 1
    assert async_order(handler).order_id == 1


def rate_limited(value: str) -> tuple[Handler, list[str]]:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.method)
        return httpx.Response(429, headers={"retry-after": value})

    return handler, calls


@pytest.mark.parametrize("value", ["61", "9" * 400, "Fri, 31 Dec 9999 23:59:59 GMT"])
def test_retry_after_above_the_maximum_raises_at_once(value: str, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(time, "sleep", pytest.fail)
    handler, calls = rate_limited(value)
    with pytest.raises(RateLimitedError) as caught:
        client_for(handler).orders.get(1)
    assert caught.value.retry_after == value
    assert calls == ["GET"]


def test_retry_after_at_the_maximum_is_waited_for(monkeypatch: pytest.MonkeyPatch) -> None:
    slept: list[float] = []
    monkeypatch.setattr(time, "sleep", slept.append)
    handler, calls = rate_limited("7")
    with pytest.raises(RateLimitedError):
        client_for(handler, max_retry_wait=7, max_retries=1).orders.get(1)
    assert slept == [7.0]
    assert calls == ["GET", "GET"]


def test_the_maximum_does_not_apply_to_the_rate_limit_wait(monkeypatch: pytest.MonkeyPatch) -> None:
    slept: list[float] = []
    monkeypatch.setattr(time, "sleep", slept.append)
    handler, _ = rate_limited("soon")
    with pytest.raises(RateLimitedError):
        client_for(handler, rate_limit_wait=9, max_retry_wait=1, max_retries=1).orders.get(1)
    assert slept == [9]


@pytest.mark.parametrize(("value", "expected"), [("5", 5.0), ("0", 0.0), ("soon", None), ("", None), (None, None)])
def test_retry_after_values(value: Any, expected: Any) -> None:
    assert _retry_after(value) == expected


def test_retry_after_date() -> None:
    future = datetime.now(timezone.utc) + timedelta(seconds=30)
    wait = _retry_after(format_datetime(future, usegmt=True))
    assert wait is not None and 25 < wait <= 30
    assert _retry_after("Thu, 01 Jan 2015 00:00:00 GMT") is None
    assert _retry_after("Mon, 01 Jan 99999999999999999999 00:00:00 GMT") is None


def test_async_client_iterates_pages() -> None:
    pages = [
        {"next": "https://foreign.invalid/ws/orders?page=2", "results": [{"order_id": 1}]},
        {"next": None, "results": [{"order_id": 2}]},
    ]
    queries: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        queries.append(request.url.query.decode())
        return httpx.Response(200, json=pages[len(queries) - 1])

    async def run() -> list[Order]:
        async with AsyncBackMarketClient(
            TOKEN,
            user_agent="agent",
            locale="en-us",
            base_url="http://mock.invalid",
            http_transport=httpx.MockTransport(handler),
        ) as client:
            return [order async for order in client.orders.iter()]

    orders = asyncio.run(run())
    assert [order.order_id for order in orders] == [1, 2]
    assert queries == ["", "page=2"]


def test_only_gzip_is_accepted_in_sync_and_async() -> None:
    seen: list[str | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("accept-encoding"))
        return httpx.Response(200, json={"order_id": 1})

    client = client_for(handler)
    client.orders.get(1)
    client._transport.http.headers["Accept-Encoding"] = "gzip, deflate, br, zstd"
    client.orders.get(1)
    async_order(handler)
    assert seen == ["gzip", "gzip", "gzip"]
