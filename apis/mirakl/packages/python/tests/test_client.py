from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from mirakl_seller import (
    AsyncMiraklClient,
    AuthenticationError,
    AuthRequest,
    BadRequestError,
    Credentials,
    HttpError,
    JobTimeoutError,
    MiraklClient,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    models,
)
from mirakl_seller._resources import OPERATIONS

KEY = "synthetic-unit-shop-key"
BASE = "https://marketplace.example.test"
Handler = Callable[[httpx.Request], httpx.Response]


def client_for(handler: Handler, **options: Any) -> MiraklClient:
    options.setdefault("base_url", BASE)
    return MiraklClient(KEY, retry_base_delay=0, http_transport=httpx.MockTransport(handler), **options)


def async_client_for(handler: Handler, **options: Any) -> AsyncMiraklClient:
    options.setdefault("base_url", BASE)
    return AsyncMiraklClient(KEY, retry_base_delay=0, http_transport=httpx.MockTransport(handler), **options)


def recording(*responses: httpx.Response) -> tuple[Handler, list[httpx.Request]]:
    sent: list[httpx.Request] = []
    remaining = iter(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return next(remaining)

    return handler, sent


def test_every_operation_has_a_public_method_that_names_its_code() -> None:
    client = client_for(lambda request: httpx.Response(200))
    assert len(OPERATIONS) == 117
    for operation in OPERATIONS.values():
        method = getattr(getattr(client, operation.resource), operation.name)
        assert f"({operation.id})" in (method.__doc__ or ""), operation.id
        if operation.iterator:
            assert callable(getattr(getattr(client, operation.resource), operation.iterator))
    assert sum(1 for operation in OPERATIONS.values() if operation.iterator) == 21
    jobs = {operation.id for operation in OPERATIONS.values() if operation.job}
    assert jobs == {"OF02", "P42", "STO02", "OF53", "OR14", "TL04"}
    for operation_id in jobs:
        operation = OPERATIONS[operation_id]
        assert callable(getattr(getattr(client, operation.resource), operation.name.replace("get_", "wait_for_", 1)))


def test_the_key_is_the_whole_authorization_header() -> None:
    handler, sent = recording(httpx.Response(200, json={"shop_id": 1, "shop_name": "Synthetic"}))
    shop = client_for(handler).shop.get()
    assert shop.shop_name == "Synthetic"
    assert sent[0].headers["authorization"] == KEY
    assert str(sent[0].url) == f"{BASE}/api/account"


def test_a_trailing_slash_on_the_base_url_is_dropped() -> None:
    handler, sent = recording(httpx.Response(200, json={"locales": []}))
    client_for(handler, base_url=f"{BASE}/").platform.list_locales()
    assert str(sent[0].url) == f"{BASE}/api/locales"


@pytest.mark.parametrize("base_url", ["", "marketplace.example.test", "ftp://marketplace.example.test", "https://"])
def test_the_base_url_must_be_an_http_url(base_url: str) -> None:
    with pytest.raises(ValueError, match="base_url"):
        MiraklClient(KEY, base_url=base_url)


def test_the_base_url_has_no_default() -> None:
    with pytest.raises(TypeError):
        MiraklClient(KEY)  # type: ignore[call-arg]


def test_exactly_one_of_a_key_and_credentials() -> None:
    with pytest.raises(ValueError, match="exactly one"):
        MiraklClient(base_url=BASE)
    with pytest.raises(ValueError, match="exactly one"):
        MiraklClient(KEY, base_url=BASE, credentials=Credentials())
    with pytest.raises(ValueError, match="empty"):
        MiraklClient("", base_url=BASE)


@pytest.mark.parametrize("shop_id", ["2001", True, 1.5])
def test_shop_id_must_be_an_integer(shop_id: Any) -> None:
    with pytest.raises(ValueError, match="shop_id"):
        MiraklClient(KEY, base_url=BASE, shop_id=shop_id)


def test_the_client_shop_id_is_sent_and_a_call_can_override_it() -> None:
    handler, sent = recording(
        httpx.Response(200, json={"shop_id": 2001}),
        httpx.Response(200, json={"shop_id": 2002}),
    )
    client = client_for(handler, shop_id=2001)
    client.shop.get()
    client.shop.get(shop_id=2002)
    assert [request.url.params.get_list("shop_id") for request in sent] == [["2001"], ["2002"]]


def test_no_shop_id_is_sent_without_one() -> None:
    handler, sent = recording(httpx.Response(200, json={"shop_id": 2001}))
    client_for(handler).shop.get()
    assert "shop_id" not in sent[0].url.params


def test_the_client_shop_id_reaches_every_page() -> None:
    handler, sent = recording(
        httpx.Response(200, json={"data": [{"id": "shipment-1"}], "next_page_token": "token-2"}),
        httpx.Response(200, json={"data": [{"id": "shipment-2"}], "next_page_token": None}),
    )
    shipments = list(client_for(handler, shop_id=2001).shipments.iter(limit=1))
    assert [shipment.id for shipment in shipments] == ["shipment-1", "shipment-2"]
    assert [dict(request.url.params) for request in sent] == [
        {"shop_id": "2001", "limit": "1"},
        {"shop_id": "2001", "limit": "1", "page_token": "token-2"},
    ]


def test_offset_paging_stops_at_the_total() -> None:
    handler, sent = recording(
        httpx.Response(200, json={"orders": [{"order_id": "order-1"}, {"order_id": "order-2"}], "total_count": 3}),
        httpx.Response(200, json={"orders": [{"order_id": "order-3"}], "total_count": 3}),
    )
    orders = list(client_for(handler).orders.iter(max=2))
    assert all(isinstance(order, models.OR11Response200Orders) for order in orders)
    assert [order.order_id for order in orders] == ["order-1", "order-2", "order-3"]
    assert [request.url.params.get("offset") for request in sent] == [None, "2"]


@pytest.mark.parametrize(
    ("status", "error_type"),
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (405, HttpError),
        (429, RateLimitedError),
        (500, ServerError),
    ],
)
def test_errors_carry_the_status_and_raw_body_without_the_key(status: int, error_type: type[HttpError]) -> None:
    client = client_for(lambda request: httpx.Response(status, text=f"refused {KEY}"), max_retries=0)
    with pytest.raises(error_type) as caught:
        client.shop.get()
    assert type(caught.value) is error_type
    assert caught.value.status == status
    assert caught.value.raw_body == "refused ***"


def test_the_key_never_reaches_the_logs(caplog: pytest.LogCaptureFixture) -> None:
    client = client_for(lambda request: httpx.Response(401, text=KEY), max_retries=0)
    with caplog.at_level(logging.DEBUG, logger="mirakl_seller"), pytest.raises(AuthenticationError):
        client.orders.list()
    assert caplog.records
    assert KEY not in caplog.text


def test_a_custom_credentials_provider_replaces_the_key() -> None:
    class Partner(Credentials):
        def apply(self, request: AuthRequest) -> None:
            request.headers["Authorization"] = "Bearer synthetic-partner-token"

    handler, sent = recording(httpx.Response(200, json={"locales": []}))
    MiraklClient(
        base_url=BASE, credentials=Partner(), http_transport=httpx.MockTransport(handler)
    ).platform.list_locales()
    assert sent[0].headers["authorization"] == "Bearer synthetic-partner-token"


def test_the_health_check_returns_nothing_whatever_the_body() -> None:
    handler, sent = recording(httpx.Response(200, json={"version": "synthetic"}))
    assert client_for(handler).platform.health_check() is None
    assert sent[0].url.path == "/api/version"


def test_a_failed_import_is_returned_and_its_report_downloads() -> None:
    handler, sent = recording(
        httpx.Response(201, json={"import_id": 41}),
        httpx.Response(200, json={"import_id": 41, "status": "RUNNING"}),
        httpx.Response(200, json={"import_id": 41, "status": "FAILED", "has_error_report": True}),
        httpx.Response(200, headers={"content-type": "application/octet-stream"}, content=b"sku;error\n"),
    )
    client = client_for(handler)
    started = client.offers.import_(file=("offers.csv", b"sku;product-id\n"), import_mode="NORMAL")
    assert isinstance(started, models.OF01Response201)
    status = client.offers.wait_for_import(41, interval=0)
    assert isinstance(status, models.OF02Response200)
    assert status.status == "FAILED"
    with client.offers.download_import_error_report(41) as report:
        assert report.read() == b"sku;error\n"
    assert [request.url.path for request in sent] == [
        "/api/offers/imports",
        "/api/offers/imports/41",
        "/api/offers/imports/41",
        "/api/offers/imports/41/error_report",
    ]


def test_a_wait_stops_at_the_deadline_with_the_last_status() -> None:
    client = client_for(lambda request: httpx.Response(200, json={"status": "PENDING"}))
    with pytest.raises(JobTimeoutError) as caught:
        client.orders.wait_for_export("tracking-1", interval=0, timeout=0)
    assert caught.value.result.status == "PENDING"


def test_download_url_sends_the_key_only_to_the_base_url_origin() -> None:
    handler, sent = recording(
        httpx.Response(200, content=b"own"),
        httpx.Response(302, headers={"location": "https://files.example.test/orders.json?signature=s"}),
        httpx.Response(200, content=b"moved"),
        httpx.Response(200, content=b"other"),
    )
    client = client_for(handler)
    with client.download_url(f"{BASE}/exports/orders.json") as own:
        assert own.read() == b"own"
    with client.download_url(f"{BASE}/exports/moved.json") as moved:
        assert moved.read() == b"moved"
    with client.download_url("https://files.example.test/orders.json?signature=s") as other:
        assert other.read() == b"other"
    assert [request.headers.get("authorization") for request in sent] == [KEY, KEY, None, None]


def test_a_json_part_is_sent_compact_from_a_model_or_a_mapping() -> None:
    handler, sent = recording(
        httpx.Response(201, json={"message_id": "message-1"}),
        httpx.Response(201, json={"message_id": "message-2"}),
    )
    client = client_for(handler)
    message = {"body": "Synthetic reply", "to": [{"type": "CUSTOMER"}]}
    client.messages.reply("thread-1", message_input=message, files=[("a.txt", b"a")])  # type: ignore[arg-type]
    model = models.M12RequestMultipartFormDataMessageInput.model_validate(message)
    client.messages.reply("thread-1", message_input=model)
    for request in sent:
        body = request.read()
        assert b'name="message_input"\r\n\r\n' + json.dumps(model.to_wire(), separators=(",", ":")).encode() in body
    assert b'filename="a.txt"' in sent[0].read()


def test_the_async_client_waits_and_downloads() -> None:
    handler, sent = recording(
        httpx.Response(200, json={"import_id": "stock-1", "status": "COMPLETE", "has_error_report": False}),
        httpx.Response(200, content=b"file"),
    )

    async def run() -> None:
        async with async_client_for(handler, shop_id=7) as client:
            status = await client.offers.wait_for_stock_import("stock-1", interval=0)
            assert status.status == "COMPLETE"
            async with await client.download_url("https://files.example.test/stock.csv") as file:
                assert await file.aread() == b"file"

    asyncio.run(run())
    assert sent[0].url.params["shop_id"] == "7"
    assert "authorization" not in sent[1].headers
