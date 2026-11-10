from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from typing import Any
from uuid import UUID

import httpx
import pytest

from mercury_banking import (
    AsyncMercuryClient,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    HttpError,
    MercuryClient,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    UnprocessableError,
)
from mercury_banking._resources import OPERATIONS

TOKEN = "secret-token:synthetic-unit-token"
HOSTS = {"api": "http://api.mock.invalid/api/v1", "vault": "http://vault.mock.invalid/api/v1"}
ACCOUNT = UUID("00000000-0000-4000-8000-acc000000001")
CARD = UUID("00000000-0000-4000-8000-ca4d00000001")
Handler = Callable[[httpx.Request], httpx.Response]


def client_for(handler: Handler, **options: Any) -> MercuryClient:
    options.setdefault("hosts", HOSTS)
    return MercuryClient(TOKEN, retry_base_delay=0, http_transport=httpx.MockTransport(handler), **options)


def async_client_for(handler: Handler, **options: Any) -> AsyncMercuryClient:
    options.setdefault("hosts", HOSTS)
    return AsyncMercuryClient(TOKEN, retry_base_delay=0, http_transport=httpx.MockTransport(handler), **options)


def test_every_operation_has_a_public_method() -> None:
    client = client_for(lambda request: httpx.Response(200))
    assert len(OPERATIONS) == 89
    for operation in OPERATIONS.values():
        resource = getattr(client, operation.resource)
        assert callable(getattr(resource, operation.name))
        if operation.iterator:
            assert callable(getattr(resource, operation.iterator))
    assert sum(1 for operation in OPERATIONS.values() if operation.iterator) == 27


def test_only_the_money_moving_writes_are_idempotent() -> None:
    marked = {operation.id for operation in OPERATIONS.values() if operation.idempotency_key}
    assert marked == {"createInternalTransfer", "createTransaction", "requestSendMoney", "requestTransferMoney"}
    assert {OPERATIONS[id].idempotency_key for id in marked} == {"idempotencyKey"}


def test_the_token_is_sent_verbatim_as_a_bearer_token() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"accounts": [], "page": {}})

    client_for(handler).accounts.list()
    assert seen[0].headers["authorization"] == f"Bearer {TOKEN}"
    assert str(seen[0].url) == "http://api.mock.invalid/api/v1/accounts"


@pytest.mark.parametrize(
    ("environment", "api", "vault"),
    [
        ("production", "https://api.mercury.com/api/v1", "https://vault-api.mercury.com/api/v1"),
        ("sandbox", "https://api-sandbox.mercury.com/api/v1", "https://api-sandbox.mercury.com/api/v1"),
    ],
)
def test_each_environment_has_its_own_hosts(environment: str, api: str, vault: str) -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return httpx.Response(200, json={})

    client = client_for(handler, environment=environment, hosts=None)
    client.organization.get()
    client.cards.reveal(CARD)
    assert seen == [f"{api}/organization", f"{vault}/cards/{CARD}/reveal"]


@pytest.mark.parametrize("status", [["active", "frozen"], ("active", "frozen")])
def test_a_list_or_tuple_filter_repeats_the_query_key(status: Any) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"cards": [], "page": {}})

    kind: Any = frozenset({"virtual"})
    client_for(handler).cards.list(status=status, kind=kind)
    assert seen[0].url.params.get_list("status") == ["active", "frozen"]
    assert seen[0].url.params.get_list("kind") == ["virtual"]


def test_the_token_and_environment_are_checked() -> None:
    with pytest.raises(ValueError, match="token"):
        MercuryClient("")
    with pytest.raises(ValueError, match="environment"):
        MercuryClient(TOKEN, environment="staging")
    with pytest.raises(ValueError, match="vault"):
        MercuryClient(TOKEN, hosts={"api": "http://api.mock.invalid"})


@pytest.mark.parametrize(
    ("status", "kind"),
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (409, ConflictError),
        (422, UnprocessableError),
        (429, RateLimitedError),
        (503, ServerError),
        (413, HttpError),
    ],
)
def test_errors_keep_the_status_and_raw_body(status: int, kind: type[HttpError]) -> None:
    client = client_for(lambda request: httpx.Response(status, text="synthetic failure"), max_retries=0)
    with pytest.raises(kind) as caught:
        client.organization.get()
    assert type(caught.value) is kind
    assert caught.value.status == status
    assert caught.value.raw_body == "synthetic failure"


def test_the_token_never_reaches_errors_or_logs(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG, logger="mercury_banking")
    client = client_for(lambda request: httpx.Response(401, text=f"bad token {TOKEN}"))
    with pytest.raises(AuthenticationError) as caught:
        client.users.list()
    assert caught.value.raw_body == "bad token ***"
    assert caplog.records
    assert TOKEN not in caplog.text
    assert TOKEN not in str(caught.value)


def test_revealed_card_details_never_reach_the_logs(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG, logger="mercury_banking")
    body = {"cardNumber": "0000111122223333", "cvc": "0417"}
    card = client_for(lambda request: httpx.Response(200, json=body)).cards.reveal(CARD)
    assert card.card_number == "0000111122223333"
    assert caplog.records
    assert "0000111122223333" not in caplog.text
    assert "0417" not in caplog.text


def send_money_body(key: str) -> dict[str, Any]:
    return {
        "recipientId": "00000000-0000-4000-8000-4ec100000001",
        "amount": 1,
        "paymentMethod": "ach",
        "idempotencyKey": key,
    }


def test_a_keyed_payment_is_retried_with_the_same_body() -> None:
    bodies: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(request.content)
        return httpx.Response(503) if len(bodies) < 3 else httpx.Response(200, json={"id": "txn", "status": "pending"})

    result = client_for(handler).accounts.send_money(ACCOUNT, send_money_body("synthetic-key-1"))
    assert result.status == "pending"
    assert len(bodies) == 3
    assert len(set(bodies)) == 1
    assert json.loads(bodies[0])["idempotencyKey"] == "synthetic-key-1"


def test_a_payment_without_a_key_is_not_retried() -> None:
    calls: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(503)

    with pytest.raises(ServerError):
        client_for(handler).accounts.send_money(ACCOUNT, send_money_body(""))
    assert len(calls) == 1
    assert json.loads(calls[0].content)["idempotencyKey"] == ""


def test_a_download_asks_for_a_pdf() -> None:
    accepts: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        accepts.append(request.headers["accept"])
        if request.url.path.endswith("/pdf"):
            return httpx.Response(200, content=b"%PDF-1.4", headers={"content-type": "application/pdf"})
        return httpx.Response(200, json={})

    with client_for(handler) as client:
        with client.invoices.download_pdf(UUID("00000000-0000-4000-8000-1a4000000001")) as download:
            assert download.read() == b"%PDF-1.4"
        client.organization.get()
    assert accepts == ["application/pdf", "application/json"]


def test_an_upload_returns_the_attachment() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["content-type"].startswith("multipart/form-data; boundary=")
        return httpx.Response(200, json={"attachmentId": "att-1", "downloadUrl": "https://files.mock.invalid/att-1"})

    attachment = client_for(handler).transactions.upload_attachment(
        UUID("00000000-0000-4000-8000-7a4000000001"), file=b"synthetic receipt"
    )
    assert attachment.attachment_id == "att-1"
    assert attachment.download_url == "https://files.mock.invalid/att-1"


def test_async_iterators_follow_the_cursor() -> None:
    pages = {
        None: {"users": [{"userId": "u1"}], "page": {"nextPage": "00000000-0000-4000-8000-05e400000001"}},
        "00000000-0000-4000-8000-05e400000001": {"users": [{"userId": "u2"}], "page": {"nextPage": None}},
    }

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=pages[request.url.params.get("start_after")])

    async def walk() -> list[Any]:
        async with async_client_for(handler) as client:
            return [user.user_id async for user in client.users.iter(limit=1)]

    assert asyncio.run(walk()) == ["u1", "u2"]
