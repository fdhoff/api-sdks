from __future__ import annotations

import asyncio
import base64
import importlib
import json
import logging
import threading
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

from ebay_sell import (
    API_SCOPE,
    ENVIRONMENTS,
    AsyncEbayClient,
    AuthenticationError,
    BadRequestError,
    DecodeError,
    EbayClient,
    HttpError,
    NotFoundError,
    SigningKey,
    Token,
    authorization_url,
)
from ebay_sell.oauth import EbayCredentials

CLIENT_ID = "Synthetic-App-PRD-0000000000-00000000"
CLIENT_SECRET = "PRD-synthetic-cert-id"
RU_NAME = "Synthetic-RuName"
APP_TOKEN = "v^1.1#synthetic-app-token"
NEW_APP_TOKEN = "v^1.1#synthetic-app-token-2"
STALE_APP_TOKEN = "v^1.1#synthetic-stale-app-token"
USER_TOKEN = "v^1.1#synthetic-user-token"
NEW_USER_TOKEN = "v^1.1#synthetic-user-token-2"
REFRESH = "v^1.1#synthetic-refresh-token"
JWE = "synthetic.jwe.value"
TOKEN_PATH = "/identity/v1/oauth2/token"
HOSTS = {"api": "http://api.mock.invalid", "apiz": "http://apiz.mock.invalid", "apim": "http://apim.mock.invalid"}
BASIC = "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
MODULES = (
    "account",
    "account_v2",
    "analytics",
    "feed",
    "finances",
    "fulfillment",
    "inventory",
    "marketing",
    "metadata",
    "negotiation",
    "recommendation",
    "stores",
    "post_order",
    "feedback",
    "identity",
    "media",
    "message",
    "notification",
    "taxonomy",
    "developer_analytics",
    "key_management",
)
Handler = Callable[[httpx.Request], httpx.Response]


def client_for(handler: Handler, **options: Any) -> EbayClient:
    options.setdefault("hosts", HOSTS)
    return EbayClient(http_transport=httpx.MockTransport(handler), **options)


def async_client_for(handler: Handler, **options: Any) -> AsyncEbayClient:
    options.setdefault("hosts", HOSTS)
    return AsyncEbayClient(http_transport=httpx.MockTransport(handler), **options)


def keyed(handler: Handler, **options: Any) -> EbayClient:
    return client_for(handler, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, **options)


def form(request: httpx.Request) -> dict[str, list[str]]:
    return parse_qs(request.content.decode())


class Server:
    """Answers the token endpoint and a few operations, refusing any bearer token not in `accepted`."""

    def __init__(self, *, expires_in: int = 7200, accepted: tuple[str, ...] = ()) -> None:
        self.requests: list[httpx.Request] = []
        self.expires_in = expires_in
        self.accepted = accepted
        self.minted = 0

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if request.url.path == TOKEN_PATH:
            grant = form(request)["grant_type"][0]
            if grant == "client_credentials":
                self.minted += 1
                token = APP_TOKEN if self.minted == 1 else NEW_APP_TOKEN
                return httpx.Response(200, json={"access_token": token, "expires_in": self.expires_in})
            body: dict[str, Any] = {
                "access_token": NEW_USER_TOKEN,
                "expires_in": 7200,
                "token_type": "User Access Token",
            }
            if grant == "authorization_code":
                body |= {"refresh_token": REFRESH, "refresh_token_expires_in": 47304000}
            return httpx.Response(200, json=body)
        bearer = request.headers.get("authorization", "").removeprefix("Bearer ")
        if self.accepted and bearer not in self.accepted:
            return httpx.Response(401, json={"errors": [{"errorId": 1001, "message": "Invalid access token"}]})
        return httpx.Response(200, json={"categoryTreeId": "0", "orders": [{"orderId": "01-00001-00001"}]})

    def paths(self) -> list[str]:
        return [request.url.path for request in self.requests]

    def calls(self) -> list[httpx.Request]:
        return [request for request in self.requests if request.url.path != TOKEN_PATH]


class HeldServer(Server):
    """Holds each refused call until `parties` calls have been refused, so that every call fails before
    any refresh."""

    def __init__(self, parties: int, **options: Any) -> None:
        super().__init__(**options)
        self.barrier = threading.Barrier(parties, timeout=5)

    def __call__(self, request: httpx.Request) -> httpx.Response:
        response = super().__call__(request)
        if response.status_code == 401:
            self.barrier.wait()
        return response


def at_once(*calls: Callable[[], Any]) -> list[Any]:
    with ThreadPoolExecutor(len(calls)) as pool:
        futures = [pool.submit(call) for call in calls]
        return [future.result() for future in futures]


def grants(server: Server) -> list[str]:
    return sorted(form(request)["grant_type"][0] for request in server.requests if request.url.path == TOKEN_PATH)


def private_key_pem() -> str:
    key = ed25519.Ed25519PrivateKey.generate()
    return key.private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()
    ).decode()


def test_every_operation_has_a_public_method() -> None:
    client = client_for(lambda request: httpx.Response(200), app_token=APP_TOKEN)
    total = iterators = 0
    for name in MODULES:
        operations = importlib.import_module(f"ebay_sell.{name}._resources").OPERATIONS
        module = getattr(client, name)
        for operation in operations.values():
            resource = getattr(module, operation.resource)
            assert callable(getattr(resource, operation.name))
            if operation.iterator:
                assert callable(getattr(resource, operation.iterator))
                iterators += 1
        total += len(operations)
    assert total == 339
    assert iterators == 35


def test_an_app_operation_mints_an_app_token_once_and_reuses_it() -> None:
    server = Server()
    client = keyed(server)
    client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_GB")

    token_request = server.requests[0]
    assert token_request.url.host == "api.mock.invalid"
    assert token_request.headers["authorization"] == BASIC
    assert token_request.headers["content-type"] == "application/x-www-form-urlencoded"
    assert form(token_request) == {"grant_type": ["client_credentials"], "scope": [API_SCOPE]}
    assert server.paths().count(TOKEN_PATH) == 1
    assert [request.headers["authorization"] for request in server.calls()] == [f"Bearer {APP_TOKEN}"] * 2


def test_an_app_token_about_to_expire_is_minted_again() -> None:
    server = Server(expires_in=30)
    client = keyed(server, app_scopes=[API_SCOPE, f"{API_SCOPE}/metadata.insights"])
    client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    assert server.paths().count(TOKEN_PATH) == 2
    assert form(server.requests[0])["scope"] == [f"{API_SCOPE} {API_SCOPE}/metadata.insights"]
    assert server.calls()[1].headers["authorization"] == f"Bearer {NEW_APP_TOKEN}"


def test_a_401_on_an_app_operation_mints_a_new_app_token_and_retries() -> None:
    server = Server(accepted=(APP_TOKEN,))
    tree = keyed(server, app_token=STALE_APP_TOKEN).taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    assert tree.category_tree_id == "0"
    assert server.paths().count(TOKEN_PATH) == 1
    assert [request.headers["authorization"] for request in server.calls()] == [
        f"Bearer {STALE_APP_TOKEN}",
        f"Bearer {APP_TOKEN}",
    ]


def test_a_401_with_a_given_app_token_and_no_keyset_is_raised() -> None:
    server = Server(accepted=(APP_TOKEN,))
    with pytest.raises(AuthenticationError) as raised:
        client_for(server, app_token=STALE_APP_TOKEN).taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    assert raised.value.code == 1001
    assert TOKEN_PATH not in server.paths()


def test_a_user_operation_sends_the_user_token_never_the_app_token() -> None:
    server = Server()
    client = keyed(server, user_token=USER_TOKEN)
    client.fulfillment.orders.get("01-00001-00001")
    assert TOKEN_PATH not in server.paths()
    assert server.requests[0].headers["authorization"] == f"Bearer {USER_TOKEN}"


def test_a_user_operation_without_a_user_token_is_refused_before_sending() -> None:
    server = Server()
    with pytest.raises(ValueError, match="needs a user token"):
        keyed(server).fulfillment.orders.get("01-00001-00001")
    assert server.requests == []


def test_an_app_operation_falls_back_to_the_user_token() -> None:
    server = Server()
    client_for(server, user_token=USER_TOKEN).taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US")
    assert server.requests[0].headers["authorization"] == f"Bearer {USER_TOKEN}"


def test_a_401_refreshes_the_user_token_and_keeps_the_refresh_token() -> None:
    server = Server(accepted=(NEW_USER_TOKEN,))
    stored: list[Token] = []
    client = keyed(server, user_token=USER_TOKEN, refresh_token=REFRESH, on_token=stored.append)
    order = client.fulfillment.orders.get("01-00001-00001")
    assert order is not None
    token_request = server.requests[1]
    assert token_request.headers["authorization"] == BASIC
    assert form(token_request) == {"grant_type": ["refresh_token"], "refresh_token": [REFRESH]}
    assert server.requests[2].headers["authorization"] == f"Bearer {NEW_USER_TOKEN}"
    assert [(token.access_token, token.refresh_token) for token in stored] == [(NEW_USER_TOKEN, REFRESH)]


def test_a_refresh_sends_the_user_scopes() -> None:
    server = Server()
    scopes = [f"{API_SCOPE}/sell.fulfillment"]
    keyed(server, refresh_token=REFRESH, user_scopes=scopes).oauth.refresh()
    assert form(server.requests[0])["scope"] == scopes


def test_without_a_refresh_token_a_401_on_a_user_operation_is_raised() -> None:
    server = Server(accepted=(NEW_USER_TOKEN,))
    with pytest.raises(AuthenticationError):
        keyed(server, user_token=USER_TOKEN).fulfillment.orders.get("01-00001-00001")
    assert TOKEN_PATH not in server.paths()


def test_a_failed_refresh_raises_its_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == TOKEN_PATH:
            return httpx.Response(400, json={"error": "invalid_grant"})
        return httpx.Response(401)

    with pytest.raises(BadRequestError) as raised:
        keyed(handler, user_token=USER_TOKEN, refresh_token=REFRESH).fulfillment.orders.get("01-00001-00001")
    assert REFRESH not in f"{raised.value} {raised.value.raw_body}"


def test_a_token_response_without_a_token_is_a_decode_error() -> None:
    client = keyed(lambda request: httpx.Response(200, json={"expires_in": 7200}))
    with pytest.raises(DecodeError):
        client.oauth.app_token()


def test_exchange_code_sends_the_ru_name_and_stores_the_token() -> None:
    server = Server()
    stored: list[Token] = []
    client = keyed(server, ru_name=RU_NAME, on_token=stored.append)
    token = client.oauth.exchange_code("v^1.1#synthetic-code")
    assert form(server.requests[0]) == {
        "grant_type": ["authorization_code"],
        "code": ["v^1.1#synthetic-code"],
        "redirect_uri": [RU_NAME],
    }
    assert server.requests[0].headers["authorization"] == BASIC
    assert (token.access_token, token.refresh_token, token.refresh_token_expires_in) == (
        NEW_USER_TOKEN,
        REFRESH,
        47304000,
    )
    assert stored == [token]
    client.fulfillment.orders.get("01-00001-00001")
    assert server.requests[1].headers["authorization"] == f"Bearer {NEW_USER_TOKEN}"


def test_exchange_code_needs_the_ru_name_and_keyset() -> None:
    with pytest.raises(ValueError, match="ru_name"):
        keyed(Server()).oauth.exchange_code("code")
    with pytest.raises(ValueError, match="client_id"):
        client_for(Server(), user_token=USER_TOKEN, ru_name=RU_NAME).oauth.authorization_url([API_SCOPE])


@pytest.mark.parametrize(
    ("environment", "host"), [("production", "auth.ebay.com"), ("sandbox", "auth.sandbox.ebay.com")]
)
def test_authorization_url_carries_the_ru_name_scopes_and_state(environment: str, host: str) -> None:
    scopes = [f"{API_SCOPE}/sell.inventory", f"{API_SCOPE}/sell.fulfillment"]
    request = keyed(Server(), ru_name=RU_NAME, environment=environment).oauth.authorization_url(scopes)
    url = urlsplit(request.url)
    query = parse_qs(url.query)
    assert (url.scheme, url.netloc, url.path) == ("https", host, "/oauth2/authorize")
    assert query == {
        "client_id": [CLIENT_ID],
        "redirect_uri": [RU_NAME],
        "response_type": ["code"],
        "scope": [" ".join(scopes)],
        "state": [request.state],
    }
    assert len(request.state) >= 32
    assert request.state != keyed(Server(), ru_name=RU_NAME).oauth.authorization_url(scopes).state


def test_authorization_url_keeps_a_given_state_and_prompt() -> None:
    request = authorization_url(CLIENT_ID, RU_NAME, [API_SCOPE], state="synthetic-state", prompt="login")
    query = parse_qs(urlsplit(request.url).query)
    assert (request.state, query["state"], query["prompt"]) == ("synthetic-state", ["synthetic-state"], ["login"])
    with pytest.raises(ValueError):
        authorization_url(CLIENT_ID, RU_NAME, [])
    with pytest.raises(ValueError):
        authorization_url(CLIENT_ID, RU_NAME, [API_SCOPE], environment="staging")


@pytest.mark.parametrize("environment", ["production", "sandbox"])
def test_each_operation_goes_to_its_host_in_the_environment(environment: str) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    client = EbayClient(user_token=USER_TOKEN, environment=environment, http_transport=httpx.MockTransport(handler))
    client.fulfillment.orders.get("01-00001-00001")
    client.finances.seller_funds.get_summary()
    hosts = ENVIRONMENTS[environment]
    assert [str(request.url.copy_with(path="/", query=None)) for request in seen] == [
        f"{hosts['api']}/",
        f"{hosts['apiz']}/",
    ]


def test_an_unknown_environment_is_refused() -> None:
    with pytest.raises(ValueError):
        EbayClient(user_token=USER_TOKEN, environment="staging")


def test_header_defaults_apply_unless_a_call_passes_its_own() -> None:
    server = Server()
    client = client_for(server, user_token=USER_TOKEN, marketplace_id="EBAY_US", content_language="en-US")
    client.account.advertising_eligibility.get()
    client.account.advertising_eligibility.get(x_ebay_c_marketplace_id="EBAY_DE")
    client.inventory.inventory_items.create_or_replace("SKU-1", {"availability": {}})
    first, second, third = server.requests
    assert first.headers["x-ebay-c-marketplace-id"] == "EBAY_US"
    assert second.headers["x-ebay-c-marketplace-id"] == "EBAY_DE"
    assert "content-language" not in first.headers
    assert third.headers["content-language"] == "en-US"


def test_a_post_order_upload_sends_the_user_token_marketplace_and_a_json_file() -> None:
    server = Server()
    client = client_for(server, user_token=USER_TOKEN, marketplace_id="EBAY_GB")
    client.post_order.returns.upload_file("5000000001", {"data": "c3ludGhldGlj", "filePurpose": "LABEL_RELATED"})
    (request,) = server.requests
    assert request.url == "http://api.mock.invalid/post-order/v2/return/5000000001/file/upload"
    assert request.headers["authorization"] == f"Bearer {USER_TOKEN}"
    assert request.headers["x-ebay-c-marketplace-id"] == "EBAY_GB"
    assert request.headers["content-type"] == "application/json"
    assert json.loads(request.content) == {"data": "c3ludGhldGlj", "filePurpose": "LABEL_RELATED"}


def test_a_signing_key_signs_each_request() -> None:
    server = Server()
    key = SigningKey(private_key=private_key_pem(), jwe=JWE)
    client = client_for(server, user_token=USER_TOKEN, signing_key=key)
    client.inventory.inventory_items.create_or_replace("SKU-1", {"availability": {}}, content_language="en-US")
    client.fulfillment.orders.get("01-00001-00001")
    with_body, without_body = server.requests
    assert with_body.headers["x-ebay-signature-key"] == JWE
    assert with_body.headers["content-digest"].startswith("sha-256=:")
    assert with_body.headers["signature-input"].startswith(
        'sig1=("content-digest" "x-ebay-signature-key" "@method" "@path" "@authority");created='
    )
    assert with_body.headers["signature"].startswith("sig1=:")
    assert without_body.headers["signature-input"].startswith(
        'sig1=("x-ebay-signature-key" "@method" "@path" "@authority");created='
    )
    assert "content-digest" not in without_body.headers


def test_a_signing_key_takes_the_bare_body_key_management_returns() -> None:
    lines = private_key_pem().strip().splitlines()[1:-1]
    signer = SigningKey(private_key="".join(lines), jwe=JWE).signer()
    assert signer.algorithm == "ed25519"
    assert "".join(lines) not in repr(SigningKey(private_key="".join(lines), jwe=JWE))


def test_errors_carry_the_errors_list() -> None:
    body = {
        "errors": [
            {
                "errorId": 35001,
                "domain": "API_INVENTORY",
                "subdomain": "Selling",
                "category": "REQUEST",
                "message": "Synthetic item not found",
                "longMessage": "Synthetic long message",
                "parameters": [{"name": "sku", "value": "SKU-1"}],
            },
            {"errorId": "not-a-number", "message": 2},
        ]
    }
    client = client_for(lambda request: httpx.Response(404, json=body), user_token=USER_TOKEN)
    with pytest.raises(NotFoundError) as raised:
        client.inventory.inventory_items.get("SKU-1")
    error = raised.value
    assert (error.status, error.code, error.message) == (404, 35001, "Synthetic item not found")
    assert error.errors[0].domain == "API_INVENTORY"
    assert error.errors[0].long_message == "Synthetic long message"
    assert [(parameter.name, parameter.value) for parameter in error.errors[0].parameters] == [("sku", "SKU-1")]
    assert (error.errors[1].error_id, error.errors[1].message) == (None, None)
    assert "Synthetic item not found" in str(error)


def test_an_error_body_that_is_not_json_is_still_typed() -> None:
    client = client_for(lambda request: httpx.Response(503, text="Service Unavailable"), user_token=USER_TOKEN)
    with pytest.raises(HttpError) as raised:
        client.inventory.inventory_items.create_or_replace("SKU-1", {"availability": {}})
    assert (raised.value.status, raised.value.errors, raised.value.raw_body) == (503, (), "Service Unavailable")


def test_the_iterator_follows_the_next_link() -> None:
    offsets: list[str | None] = []

    def handler(request: httpx.Request) -> httpx.Response:
        offset = request.url.params.get("offset")
        offsets.append(offset)
        if offset is None:
            next_link = "https://api.ebay.com/sell/fulfillment/v1/order?limit=2&offset=2"
            return httpx.Response(200, json={"orders": [{"orderId": "1"}, {"orderId": "2"}], "next": next_link})
        return httpx.Response(200, json={"orders": [{"orderId": "3"}]})

    orders = list(client_for(handler, user_token=USER_TOKEN).fulfillment.orders.iter(limit="2"))
    assert [order.order_id for order in orders] == ["1", "2", "3"]
    assert offsets == [None, "2"]


def test_logs_and_errors_never_hold_a_secret(caplog: pytest.LogCaptureFixture) -> None:
    pem = private_key_pem()
    secrets = (CLIENT_SECRET, BASIC.removeprefix("Basic "), APP_TOKEN, USER_TOKEN, NEW_USER_TOKEN, REFRESH)
    echoed = " ".join(secrets)

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == TOKEN_PATH:
            return Server()(request)
        return httpx.Response(403, text=f"{echoed} {request.headers.get('authorization')} {pem}")

    client = keyed(
        handler,
        app_token=APP_TOKEN,
        user_token=USER_TOKEN,
        refresh_token=REFRESH,
        signing_key=SigningKey(private_key=pem, jwe=JWE),
    )
    client.oauth.refresh()
    with caplog.at_level(logging.DEBUG, logger="ebay_sell"), pytest.raises(HttpError) as raised:
        client.fulfillment.orders.get("01-00001-00001")
    text = f"{raised.value} {raised.value.raw_body} {caplog.text} {client.oauth!r}"
    assert caplog.records
    assert not [secret for secret in secrets if secret in text]
    assert pem.splitlines()[1] not in text


def test_token_repr_hides_the_tokens() -> None:
    text = repr(Token(USER_TOKEN, 7200, REFRESH))
    assert USER_TOKEN not in text
    assert REFRESH not in text


def test_credentials_are_required() -> None:
    with pytest.raises(ValueError):
        EbayClient()
    with pytest.raises(ValueError):
        EbayClient(client_id=CLIENT_ID)
    assert CLIENT_SECRET not in repr(EbayCredentials(CLIENT_ID, CLIENT_SECRET, None, None, None, None))


def test_app_scopes_cannot_be_empty() -> None:
    for scopes in ((), ("",), (" ",)):
        for client in (EbayClient, AsyncEbayClient):
            with pytest.raises(ValueError, match="app_scopes needs at least one scope"):
                client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, app_scopes=scopes)


def test_concurrent_first_calls_share_one_app_token() -> None:
    server = Server()
    with keyed(server) as client:
        trees = at_once(
            *(lambda: client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US") for _ in range(4))
        )
    assert [tree.category_tree_id for tree in trees] == ["0"] * 4
    assert grants(server) == ["client_credentials"]


def test_concurrent_401s_share_one_refresh() -> None:
    server = HeldServer(3, accepted=(NEW_USER_TOKEN,))
    with keyed(server, user_token=USER_TOKEN, refresh_token=REFRESH) as client:
        at_once(*(lambda: client.fulfillment.orders.get("01-00001-00001") for _ in range(3)))
    assert grants(server) == ["refresh_token"]


def test_an_app_401_and_a_user_401_at_once_each_refresh_their_own_token() -> None:
    server = HeldServer(2, accepted=(APP_TOKEN, NEW_USER_TOKEN))
    with keyed(server, app_token=STALE_APP_TOKEN, user_token=USER_TOKEN, refresh_token=REFRESH) as client:
        at_once(
            lambda: client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US"),
            lambda: client.fulfillment.orders.get("01-00001-00001"),
        )
    assert grants(server) == ["client_credentials", "refresh_token"]


def test_async_concurrent_calls_share_one_app_token() -> None:
    server = Server()

    async def run() -> list[str | None]:
        async with async_client_for(server, client_id=CLIENT_ID, client_secret=CLIENT_SECRET) as client:
            trees = await asyncio.gather(
                *(client.taxonomy.category_trees.get_default_id(marketplace_id="EBAY_US") for _ in range(3))
            )
            return [tree.category_tree_id for tree in trees]

    assert asyncio.run(run()) == ["0", "0", "0"]
    assert server.paths().count(TOKEN_PATH) == 1


def test_async_concurrent_401s_share_one_refresh() -> None:
    server = Server(accepted=(NEW_USER_TOKEN,))
    stored: list[Token] = []

    async def run() -> None:
        async with async_client_for(
            server,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_token=USER_TOKEN,
            refresh_token=REFRESH,
            on_token=stored.append,
        ) as client:
            await asyncio.gather(*(client.fulfillment.orders.get("01-00001-00001") for _ in range(3)))

    asyncio.run(run())
    assert server.paths().count(TOKEN_PATH) == 1
    assert len(stored) == 1


def test_async_exchange_code_and_iterator() -> None:
    server = Server()

    async def run() -> list[str | None]:
        async with async_client_for(
            server, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, ru_name=RU_NAME
        ) as client:
            await client.oauth.exchange_code("v^1.1#synthetic-code")
            return [order.order_id async for order in client.fulfillment.orders.iter()]

    assert asyncio.run(run()) == ["01-00001-00001"]
    assert server.requests[1].headers["authorization"] == f"Bearer {NEW_USER_TOKEN}"
