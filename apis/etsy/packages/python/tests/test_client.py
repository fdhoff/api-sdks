from __future__ import annotations

import asyncio
import base64
import hashlib
import logging
import threading
import time
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest

from etsy_seller import (
    AsyncEtsyClient,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    DecodeError,
    EtsyClient,
    HttpError,
    Token,
    authorization_url,
)
from etsy_seller._resources import OPERATIONS
from etsy_seller.models import ShopListing
from etsy_seller.oauth import EtsyCredentials

KEY = "synthetic-keystring"
SECRET = "synthetic-shared-secret"
ACCESS = "12345678.synthetic-access"
REFRESH = "12345678.synthetic-refresh"
NEW_ACCESS = "12345678.synthetic-access-2"
NEW_REFRESH = "12345678.synthetic-refresh-2"
TOKEN_PATH = "/v3/public/oauth/token"
Handler = Callable[[httpx.Request], httpx.Response]


def client_for(handler: Handler, **options: Any) -> EtsyClient:
    return EtsyClient(
        KEY, SECRET, base_url="http://mock.invalid", http_transport=httpx.MockTransport(handler), **options
    )


def async_client_for(handler: Handler, **options: Any) -> AsyncEtsyClient:
    return AsyncEtsyClient(
        KEY, SECRET, base_url="http://mock.invalid", http_transport=httpx.MockTransport(handler), **options
    )


def form(request: httpx.Request) -> dict[str, list[str]]:
    return parse_qs(request.content.decode())


def new_token(request: httpx.Request) -> httpx.Response:
    body = {"access_token": NEW_ACCESS, "refresh_token": NEW_REFRESH, "expires_in": 3600, "token_type": "Bearer"}
    return httpx.Response(200, json=body)


class Expiring:
    """Answers 401 until the access token is the refreshed one, and records every request."""

    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if request.url.path == TOKEN_PATH:
            return new_token(request)
        if request.headers.get("authorization") != f"Bearer {NEW_ACCESS}":
            return httpx.Response(401, json={"error": "invalid_token"})
        return httpx.Response(200, json={"user_id": 12345678, "shop_id": 1})

    def paths(self) -> list[str]:
        return [request.url.path for request in self.requests]


def test_every_operation_has_a_public_method() -> None:
    client = client_for(lambda request: httpx.Response(200))
    assert len(OPERATIONS) == 107
    for operation in OPERATIONS.values():
        resource = getattr(client, operation.resource)
        assert callable(getattr(resource, operation.name))
        if operation.iterator:
            assert callable(getattr(resource, operation.iterator))
    assert sum(1 for operation in OPERATIONS.values() if operation.iterator) == 16


def test_key_only_operations_send_no_access_token() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"application_id": 1})

    client_for(handler, access_token=ACCESS).application.ping()
    assert seen[0].headers["x-api-key"] == f"{KEY}:{SECRET}"
    assert "authorization" not in seen[0].headers


def test_oauth_operations_send_both_headers() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"user_id": 12345678, "shop_id": 1})

    me = client_for(handler, access_token=ACCESS).users.get_me()
    assert me.user_id == 12345678
    assert seen[0].headers["x-api-key"] == f"{KEY}:{SECRET}"
    assert seen[0].headers["authorization"] == f"Bearer {ACCESS}"


def test_form_bodies_are_url_encoded_with_repeated_fields() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(201, json={"listing_id": 1})

    listing = client_for(handler, access_token=ACCESS).listings.create_draft(
        1,
        quantity=1,
        title="Synthetic listing",
        description="Synthetic description",
        price=1.5,
        who_made="i_did",
        when_made="made_to_order",
        taxonomy_id=1,
        tags=["one", "two"],
        is_supply=False,
    )
    assert isinstance(listing, ShopListing)
    assert seen[0].headers["content-type"] == "application/x-www-form-urlencoded"
    fields = form(seen[0])
    assert fields["tags"] == ["one", "two"]
    assert fields["price"] == ["1.5"]
    assert fields["is_supply"] == ["false"]
    assert "shipping_profile_id" not in fields


def test_offset_iterator_walks_every_page() -> None:
    offsets: list[str | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        offsets.append(request.url.params.get("offset"))
        pages = {None: [{"listing_id": 1}, {"listing_id": 2}], "2": [{"listing_id": 3}]}
        return httpx.Response(200, json={"count": 3, "results": pages[request.url.params.get("offset")]})

    listings = list(client_for(handler).listings.iter_active(limit=2))
    assert [listing.listing_id for listing in listings] == [1, 2, 3]
    assert offsets == [None, "2"]


@pytest.mark.parametrize(("status", "kind"), [(409, ConflictError), (401, AuthenticationError)])
def test_errors_carry_the_body_message(status: int, kind: type[HttpError]) -> None:
    client = client_for(lambda request: httpx.Response(status, json={"error": "Synthetic failure"}))
    with pytest.raises(kind) as raised:
        client.shops.get(1)
    assert raised.value.message == "Synthetic failure"
    assert raised.value.status == status


def test_a_401_refreshes_once_then_retries_with_the_new_token() -> None:
    handler = Expiring()
    stored: list[Token] = []
    client = client_for(handler, access_token=ACCESS, refresh_token=REFRESH, on_token=stored.append)

    assert client.users.get_me().shop_id == 1
    assert handler.paths() == ["/v3/application/users/me", TOKEN_PATH, "/v3/application/users/me"]
    refresh = handler.requests[1]
    assert form(refresh) == {"grant_type": ["refresh_token"], "client_id": [KEY], "refresh_token": [REFRESH]}
    assert "x-api-key" not in refresh.headers
    assert "authorization" not in refresh.headers
    assert [(token.access_token, token.refresh_token, token.expires_in) for token in stored] == [
        (NEW_ACCESS, NEW_REFRESH, 3600)
    ]

    client.users.get_me()
    assert handler.paths()[3:] == ["/v3/application/users/me"]


def test_a_second_401_after_a_refresh_is_raised() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        if request.url.path == TOKEN_PATH:
            return new_token(request)
        return httpx.Response(401, json={"error": "invalid_token"})

    with pytest.raises(AuthenticationError):
        client_for(handler, access_token=ACCESS, refresh_token=REFRESH).users.get_me()
    assert calls == ["/v3/application/users/me", TOKEN_PATH, "/v3/application/users/me"]


def test_a_401_on_a_key_only_operation_does_not_refresh() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        return httpx.Response(401, json={"error": "invalid_api_key"})

    with pytest.raises(AuthenticationError):
        client_for(handler, access_token=ACCESS, refresh_token=REFRESH).application.ping()
    assert calls == ["/v3/application/openapi-ping"]


def test_without_a_refresh_token_a_401_is_raised() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        return httpx.Response(401, json={"error": "invalid_token"})

    client = client_for(handler, access_token=ACCESS)
    with pytest.raises(AuthenticationError):
        client.users.get_me()
    assert calls == ["/v3/application/users/me"]
    with pytest.raises(ValueError):
        client.oauth.refresh()


def test_a_failed_refresh_raises_its_error_without_the_refresh_token() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == TOKEN_PATH:
            return httpx.Response(400, json={"error": "invalid_grant", "error_description": f"bad {REFRESH}"})
        return httpx.Response(401, json={"error": "invalid_token"})

    with pytest.raises(BadRequestError) as raised:
        client_for(handler, access_token=ACCESS, refresh_token=REFRESH).users.get_me()
    assert raised.value.message == "invalid_grant"
    assert raised.value.raw_body is not None
    assert REFRESH not in raised.value.raw_body


def test_a_401_from_the_token_endpoint_is_raised_without_another_refresh() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        return httpx.Response(401, json={"error": "invalid_client"})

    with pytest.raises(AuthenticationError) as raised:
        client_for(handler, access_token=ACCESS, refresh_token=REFRESH).users.get_me()
    assert raised.value.message == "invalid_client"
    assert calls == ["/v3/application/users/me", TOKEN_PATH]


def test_a_token_response_without_tokens_is_a_decode_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"token_type": "Bearer"})

    with pytest.raises(DecodeError):
        client_for(handler, refresh_token=REFRESH).oauth.refresh()


def test_exchange_code_stores_the_token_for_later_calls() -> None:
    seen: list[httpx.Request] = []
    stored: list[Token] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.path == TOKEN_PATH:
            return new_token(request)
        return httpx.Response(200, json={"user_id": 12345678, "shop_id": 1})

    client = client_for(handler, on_token=stored.append)
    token = client.oauth.exchange_code(
        "synthetic-code", code_verifier="v" * 43, redirect_uri="https://example.com/callback"
    )
    assert token.user_id == 12345678
    assert stored == [token]
    assert form(seen[0]) == {
        "grant_type": ["authorization_code"],
        "client_id": [KEY],
        "redirect_uri": ["https://example.com/callback"],
        "code": ["synthetic-code"],
        "code_verifier": ["v" * 43],
    }
    client.users.get_me()
    assert seen[1].headers["authorization"] == f"Bearer {NEW_ACCESS}"


def test_logs_and_errors_never_hold_a_secret(caplog: pytest.LogCaptureFixture) -> None:
    secrets = (KEY, SECRET, ACCESS, REFRESH, NEW_ACCESS, NEW_REFRESH)
    echoed = " ".join(secrets)

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == TOKEN_PATH:
            return new_token(request)
        return httpx.Response(403, text=f"{echoed} {request.headers.get('authorization')}")

    client = client_for(handler, access_token=ACCESS, refresh_token=REFRESH)
    client.oauth.refresh()
    with caplog.at_level(logging.DEBUG, logger="etsy_seller"), pytest.raises(HttpError) as raised:
        client.users.get_me()
    text = f"{raised.value} {raised.value.raw_body} {caplog.text} {client.oauth!r}"
    assert caplog.records
    assert not [secret for secret in secrets if secret in text]


def test_token_repr_hides_the_tokens() -> None:
    text = repr(Token(ACCESS, REFRESH, 3600))
    assert ACCESS not in text
    assert REFRESH not in text


def test_authorization_url_uses_pkce_s256_and_state() -> None:
    request = authorization_url(KEY, "https://example.com/callback", ["listings_r", "shops_r"])
    query = parse_qs(urlsplit(request.url).query)
    digest = hashlib.sha256(request.code_verifier.encode()).digest()
    assert request.url.startswith("https://www.etsy.com/oauth/connect?")
    assert query == {
        "response_type": ["code"],
        "client_id": [KEY],
        "redirect_uri": ["https://example.com/callback"],
        "scope": ["listings_r shops_r"],
        "state": [request.state],
        "code_challenge": [base64.urlsafe_b64encode(digest).rstrip(b"=").decode()],
        "code_challenge_method": ["S256"],
    }
    assert 43 <= len(request.code_verifier) <= 128
    assert request.code_verifier not in repr(request)
    other = authorization_url(KEY, "https://example.com/callback", ["listings_r"])
    assert other.state != request.state
    assert other.code_verifier != request.code_verifier


def test_authorization_url_keeps_a_given_state_and_rejects_a_bad_verifier() -> None:
    client = client_for(lambda request: httpx.Response(200))
    request = client.oauth.authorization_url("https://example.com/callback", ["shops_r"], state="synthetic-state")
    assert request.state == "synthetic-state"
    with pytest.raises(ValueError):
        authorization_url(KEY, "https://example.com/callback", ["shops_r"], code_verifier="short")
    with pytest.raises(ValueError):
        authorization_url(KEY, "https://example.com/callback", [])


def test_credentials_are_required() -> None:
    with pytest.raises(ValueError):
        EtsyClient("", SECRET)


def test_async_concurrent_401s_share_one_refresh() -> None:
    handler = Expiring()
    stored: list[Token] = []

    async def run() -> list[int | None]:
        async with async_client_for(
            handler, access_token=ACCESS, refresh_token=REFRESH, on_token=stored.append
        ) as client:
            results = await asyncio.gather(*(client.users.get_me() for _ in range(3)))
            return [me.shop_id for me in results]

    assert asyncio.run(run()) == [1, 1, 1]
    assert handler.paths().count(TOKEN_PATH) == 1
    assert len(stored) == 1


def test_an_explicit_refresh_and_a_401_share_one_token_request() -> None:
    requests: list[httpx.Request] = []
    token_started = threading.Event()

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path == TOKEN_PATH:
            token_started.set()
            time.sleep(0.2)
        elif request.headers.get("authorization") == f"Bearer {ACCESS}":
            token_started.wait(5)
        return Expiring()(request)

    client = client_for(handler, access_token=ACCESS, refresh_token=REFRESH)
    explicit = threading.Thread(target=client.oauth.refresh)
    explicit.start()
    assert client.users.get_me().shop_id == 1
    explicit.join()
    assert [form(request)["refresh_token"] for request in requests if request.url.path == TOKEN_PATH] == [[REFRESH]]


def test_async_explicit_refresh_and_a_401_share_one_token_request() -> None:
    handler = Expiring()

    async def slow(request: httpx.Request) -> httpx.Response:
        if request.url.path == TOKEN_PATH:
            await asyncio.sleep(0.01)
        return handler(request)

    async def run() -> tuple[Token, int | None]:
        async with AsyncEtsyClient(
            KEY,
            SECRET,
            base_url="http://mock.invalid",
            http_transport=httpx.MockTransport(slow),
            access_token=ACCESS,
            refresh_token=REFRESH,
        ) as client:
            token, me = await asyncio.gather(client.oauth.refresh(), client.users.get_me())
            return token, me.shop_id

    token, shop_id = asyncio.run(run())
    assert token.access_token == NEW_ACCESS
    assert shop_id == 1
    assert handler.paths().count(TOKEN_PATH) == 1


def test_credentials_keep_only_recent_values_for_redaction() -> None:
    credentials = EtsyCredentials(KEY, SECRET, ACCESS, None, None)
    credentials.remember(*(f"synthetic-old-{index}" for index in range(100)))
    secrets = list(credentials.secrets())
    assert len(secrets) < 20
    assert {KEY, SECRET, "synthetic-old-99"} <= set(secrets)
    assert ACCESS not in secrets


def test_async_exchange_code_and_form_bodies() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.path == TOKEN_PATH:
            return new_token(request)
        return httpx.Response(200, json={"shop_section_id": 1, "title": "Synthetic"})

    async def run() -> None:
        async with async_client_for(handler) as client:
            await client.oauth.exchange_code("synthetic-code", code_verifier="v" * 43, redirect_uri="https://e.test")
            await client.shop_sections.create(1, title="Synthetic")

    asyncio.run(run())
    assert form(seen[1]) == {"title": ["Synthetic"]}
    assert seen[1].headers["authorization"] == f"Bearer {NEW_ACCESS}"
