from __future__ import annotations

import asyncio
import base64
import logging
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from gitea_rest import (
    AsyncGiteaClient,
    AuthenticationError,
    AuthRequest,
    BadRequestError,
    ConflictError,
    Credentials,
    DecodeError,
    GiteaClient,
    HttpError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    UnprocessableError,
    models,
)
from gitea_rest._resources import OPERATIONS

TOKEN = "synthetic-unit-access-token"
PASSWORD = "synthetic-unit-password"
OTP = "482913"
BASE = "https://gitea.example.test"
OTHER = "https://root-url.example.test"
Handler = Callable[[httpx.Request], httpx.Response]


def client_for(handler: Handler, *, token: str | None = TOKEN, **options: Any) -> GiteaClient:
    options.setdefault("base_url", BASE)
    return GiteaClient(token, retry_base_delay=0, http_transport=httpx.MockTransport(handler), **options)


def recording(*responses: httpx.Response) -> tuple[Handler, list[httpx.Request]]:
    sent: list[httpx.Request] = []
    remaining = iter(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return next(remaining)

    return handler, sent


def page(body: Any, next_page: str | None = None, **extra: str) -> httpx.Response:
    links = [f'<{OTHER}/api/v1/user/repos?{query}>; rel="{rel}"' for rel, query in extra.items()]
    if next_page is not None:
        links.insert(0, f'<{OTHER}/api/v1/user/repos?{next_page}>; rel="next"')
    return httpx.Response(200, json=body, headers={"link": ", ".join(links)} if links else {})


def test_every_operation_has_a_public_method_that_names_its_operation_id() -> None:
    client = client_for(lambda request: httpx.Response(200))
    assert len(OPERATIONS) == 533
    for operation in OPERATIONS.values():
        method = getattr(getattr(client, operation.resource), operation.name)
        assert f"({operation.id})" in (method.__doc__ or ""), operation.id
        if operation.iterator:
            assert callable(getattr(getattr(client, operation.resource), operation.iterator))
    assert sum(1 for operation in OPERATIONS.values() if operation.iterator) == 110


@pytest.mark.parametrize(
    ("base_url", "url"),
    [
        (BASE, f"{BASE}/api/v1/version"),
        (f"{BASE}/", f"{BASE}/api/v1/version"),
        ("https://example.test/git", "https://example.test/git/api/v1/version"),
        ("http://localhost:3000", "http://localhost:3000/api/v1/version"),
    ],
)
def test_the_client_adds_api_v1_to_the_instance_url(base_url: str, url: str) -> None:
    handler, sent = recording(httpx.Response(200, json={"version": "0.0.0-synthetic"}))
    assert client_for(handler, base_url=base_url).misc.get_version().version == "0.0.0-synthetic"
    assert str(sent[0].url) == url


@pytest.mark.parametrize("base_url", ["", "gitea.example.test", "ftp://gitea.example.test", "https://"])
def test_the_base_url_must_be_an_http_url(base_url: str) -> None:
    with pytest.raises(ValueError, match="base_url"):
        GiteaClient(TOKEN, base_url=base_url)


@pytest.mark.parametrize("base_url", [f"{BASE}/api/v1", f"{BASE}/api/v1/"])
def test_the_base_url_leaves_out_api_v1(base_url: str) -> None:
    with pytest.raises(ValueError, match="/api/v1"):
        GiteaClient(TOKEN, base_url=base_url)


def test_the_base_url_has_no_default() -> None:
    with pytest.raises(TypeError):
        GiteaClient(TOKEN)  # type: ignore[call-arg]


def test_a_token_goes_with_the_token_scheme() -> None:
    handler, sent = recording(httpx.Response(200, json={"id": 1, "login": "synthetic-user"}))
    assert client_for(handler).current_user.get().login == "synthetic-user"
    assert sent[0].headers["authorization"] == f"token {TOKEN}"
    assert "x-gitea-otp" not in sent[0].headers
    assert "sudo" not in sent[0].headers


def test_basic_sends_the_one_time_password_and_sudo() -> None:
    handler, sent = recording(httpx.Response(200, json={}), httpx.Response(200, json={}))
    client_for(handler, token=None, username="synthetic-user", password=PASSWORD).current_user.get()
    client_for(
        handler, token=None, username="synthetic-admin", password=PASSWORD, otp=OTP, sudo="other"
    ).misc.get_version()
    plain = base64.b64encode(f"synthetic-user:{PASSWORD}".encode()).decode()
    admin = base64.b64encode(f"synthetic-admin:{PASSWORD}".encode()).decode()
    assert sent[0].headers["authorization"] == f"Basic {plain}"
    assert "x-gitea-otp" not in sent[0].headers
    assert sent[1].headers["authorization"] == f"Basic {admin}"
    assert sent[1].headers["x-gitea-otp"] == OTP
    assert sent[1].headers["sudo"] == "other"


def test_sudo_goes_with_a_token() -> None:
    handler, sent = recording(httpx.Response(200, json={}))
    client_for(handler, sudo="synthetic-other-user").current_user.get()
    assert sent[0].headers["sudo"] == "synthetic-other-user"


@pytest.mark.parametrize(
    ("options", "match"),
    [
        ({}, "exactly one"),
        ({"token": TOKEN, "username": "u", "password": PASSWORD}, "exactly one"),
        ({"token": TOKEN, "credentials": Credentials()}, "exactly one"),
        ({"username": "u"}, "both"),
        ({"password": PASSWORD}, "both"),
        ({"token": TOKEN, "otp": OTP}, "otp"),
        ({"credentials": Credentials(), "sudo": "other"}, "credentials provider"),
        ({"token": ""}, "token must not be empty"),
        ({"username": "u", "password": ""}, "password must not be empty"),
        ({"token": TOKEN, "sudo": ""}, "sudo must not be empty"),
    ],
)
def test_credentials_are_checked(options: dict[str, Any], match: str) -> None:
    with pytest.raises(ValueError, match=match):
        GiteaClient(base_url=BASE, **options)


def test_a_custom_credentials_provider_replaces_the_others() -> None:
    class Bearer(Credentials):
        def apply(self, request: AuthRequest) -> None:
            request.headers["Authorization"] = "Bearer synthetic-oauth2-token"

    handler, sent = recording(httpx.Response(200, json={}))
    GiteaClient(base_url=BASE, credentials=Bearer(), http_transport=httpx.MockTransport(handler)).current_user.get()
    assert sent[0].headers["authorization"] == "Bearer synthetic-oauth2-token"


@pytest.mark.parametrize(
    ("status", "error_type"),
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (405, HttpError),
        (409, ConflictError),
        (422, UnprocessableError),
        (429, RateLimitedError),
        (500, ServerError),
    ],
)
def test_errors_carry_the_status_message_and_raw_body(status: int, error_type: type[HttpError]) -> None:
    body = {"message": "synthetic refusal", "url": f"{BASE}/api/swagger"}
    client = client_for(lambda request: httpx.Response(status, json=body), max_retries=0)
    with pytest.raises(error_type) as caught:
        client.repos.get("synthetic-owner", "synthetic-repo")
    assert type(caught.value) is error_type
    assert caught.value.status == status
    assert caught.value.message == "synthetic refusal"
    assert "synthetic refusal" in str(caught.value)
    assert caught.value.raw_body is not None and '"synthetic refusal"' in caught.value.raw_body


def test_an_error_that_is_not_json_has_no_message() -> None:
    client = client_for(lambda request: httpx.Response(403, text="forbidden"), max_retries=0)
    with pytest.raises(PermissionDeniedError) as caught:
        client.current_user.get()
    assert caught.value.message is None
    assert caught.value.raw_body == "forbidden"


ENCODED = base64.b64encode(f"synthetic-user:{PASSWORD}".encode()).decode()


@pytest.mark.parametrize(
    ("options", "secrets"),
    [
        ({"token": TOKEN}, [TOKEN]),
        ({"token": None, "username": "synthetic-user", "password": PASSWORD, "otp": OTP}, [PASSWORD, OTP, ENCODED]),
    ],
)
def test_no_credential_reaches_an_error_or_the_logs(
    options: dict[str, Any], secrets: list[str], caplog: pytest.LogCaptureFixture
) -> None:
    echo = " ".join(["refused", *secrets])
    client = client_for(lambda request: httpx.Response(401, json={"message": echo}), max_retries=0, **options)
    with caplog.at_level(logging.DEBUG, logger="gitea_rest"), pytest.raises(AuthenticationError) as caught:
        client.current_user.get()
    assert caught.value.message == " ".join(["refused", *["***"] * len(secrets)])
    assert caplog.records
    for secret in secrets:
        assert secret not in str(caught.value)
        assert secret not in (caught.value.raw_body or "")
        assert secret not in caplog.text


def test_a_file_path_is_one_encoded_segment() -> None:
    handler, sent = recording(httpx.Response(200, json={"type": "file", "path": "docs/guide/intro.md"}))
    client_for(handler).contents.get("synthetic-owner", "synthetic-repo", "docs/guide/intro.md", ref="main")
    assert (
        sent[0].url.raw_path
        == b"/api/v1/repos/synthetic-owner/synthetic-repo/contents/docs%2Fguide%2Fintro.md?ref=main"
    )


def test_iterators_follow_the_next_link_without_fetching_it() -> None:
    handler, sent = recording(
        page([{"id": 1}, {"id": 2}], "limit=2&page=2", last="limit=2&page=3"),
        page([{"id": 3}, {"id": 4}], "limit=2&page=3", prev="limit=2&page=1"),
        page([{"id": 5}], prev="limit=2&page=2", first="limit=2&page=1"),
    )
    repos = list(client_for(handler).current_user.iter_repos(limit=2))
    assert all(isinstance(repo, models.Repository) for repo in repos)
    assert [repo.id for repo in repos] == [1, 2, 3, 4, 5]
    assert [str(request.url) for request in sent] == [
        f"{BASE}/api/v1/user/repos?limit=2",
        f"{BASE}/api/v1/user/repos?page=2&limit=2",
        f"{BASE}/api/v1/user/repos?page=3&limit=2",
    ]


def test_an_object_page_reads_its_field() -> None:
    handler, sent = recording(
        httpx.Response(
            200, json={"ok": True, "data": [{"id": 1}]}, headers={"link": f'<{OTHER}/x?page=2>; rel="next"'}
        ),
        httpx.Response(200, json={"ok": True, "data": [{"id": 2}]}),
    )
    assert [repo.id for repo in client_for(handler).repos.iter_search(q="synthetic")] == [1, 2]
    assert [dict(request.url.params) for request in sent] == [{"q": "synthetic"}, {"q": "synthetic", "page": "2"}]


def test_a_next_link_back_to_a_page_already_sent_is_a_decode_error() -> None:
    handler, sent = recording(page([{"id": 1}], "page=2"), page([{"id": 2}], "page=1"))
    with pytest.raises(DecodeError):
        list(client_for(handler).current_user.iter_repos(page=1))
    assert len(sent) == 2


def test_the_async_client_iterates_and_raises_typed_errors() -> None:
    handler, sent = recording(
        page([{"number": 1}], "page=2"),
        page([{"number": 2}]),
        httpx.Response(404, json={"message": "synthetic not found"}),
    )

    async def run() -> None:
        async with AsyncGiteaClient(TOKEN, base_url=BASE, http_transport=httpx.MockTransport(handler)) as client:
            issues = [issue.number async for issue in client.issues.iter("synthetic-owner", "synthetic-repo")]
            assert issues == [1, 2]
            with pytest.raises(NotFoundError) as caught:
                await client.repos.get("synthetic-owner", "missing")
            assert caught.value.message == "synthetic not found"

    asyncio.run(run())
    assert [request.url.path for request in sent] == [
        "/api/v1/repos/synthetic-owner/synthetic-repo/issues",
        "/api/v1/repos/synthetic-owner/synthetic-repo/issues",
        "/api/v1/repos/synthetic-owner/missing",
    ]
