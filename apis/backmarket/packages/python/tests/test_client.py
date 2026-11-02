from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from typing import Any

import httpx
import pytest
from pydantic import ValidationError

from backmarket_seller import (
    ApiConnectionError,
    ApiError,
    AsyncBackMarketClient,
    BackMarketClient,
    DecodeError,
    Environment,
    Region,
    WafBlockedError,
)
from backmarket_seller._resources import OPERATIONS
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


def test_a_non_object_response_comes_back_raw() -> None:
    client = client_for(lambda request: httpx.Response(200, json=["unexpected"]))
    result: Any = client.orders.get(1)
    assert result == ["unexpected"]


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


@pytest.mark.parametrize(("value", "expected"), [("5", 5.0), ("0", 0.0), ("soon", None), ("", None), (None, None)])
def test_retry_after_values(value: Any, expected: Any) -> None:
    assert _retry_after(value) == expected


def test_retry_after_date() -> None:
    future = datetime.now(timezone.utc) + timedelta(seconds=30)
    wait = _retry_after(format_datetime(future, usegmt=True))
    assert wait is not None and 25 < wait <= 30
    assert _retry_after("Thu, 01 Jan 2015 00:00:00 GMT") is None


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
