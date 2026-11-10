from __future__ import annotations

import base64
import logging
from types import TracebackType
from urllib.parse import urlsplit

import httpx
from typing_extensions import Self

from ._resources import AsyncResources, Resources
from ._runtime import AsyncTransport, Credentials, Settings, StaticCredentials, SyncTransport
from .errors import to_error

logger = logging.getLogger("gitea_rest")

API_PATH = "/api/v1"


def _credentials(
    token: str | None,
    username: str | None,
    password: str | None,
    otp: str | None,
    sudo: str | None,
    credentials: Credentials | None,
) -> Credentials:
    basic = username is not None or password is not None
    if sum((token is not None, basic, credentials is not None)) != 1:
        raise ValueError("Pass exactly one of token, username and password, and credentials")
    if credentials is not None:
        if otp is not None or sudo is not None:
            raise ValueError(
                "otp and sudo go with a token or username and password; a credentials provider sets its own"
            )
        return credentials
    if otp is not None and not basic:
        raise ValueError("otp goes only with username and password")
    for name, value in (("token", token), ("username", username), ("password", password), ("otp", otp), ("sudo", sudo)):
        if value == "":
            raise ValueError(f"{name} must not be empty")
    headers: dict[str, str] = {}
    secrets: list[str] = []
    if basic:
        if username is None or password is None:
            raise ValueError("Pass both username and password")
        encoded = base64.b64encode(f"{username}:{password}".encode()).decode()
        headers["Authorization"] = f"Basic {encoded}"
        secrets += [password, encoded]
        if otp is not None:
            headers["X-GITEA-OTP"] = otp
            secrets.append(otp)
    else:
        headers["Authorization"] = f"token {token}"
        secrets.append(str(token))
    if sudo is not None:
        headers["Sudo"] = sudo
    return StaticCredentials(headers, secrets=secrets)


def _api_url(base_url: str) -> str:
    url = urlsplit(base_url)
    if url.scheme not in ("http", "https") or not url.hostname:
        raise ValueError("base_url must be your Gitea instance's URL, such as https://gitea.example.com")
    root = base_url.rstrip("/")
    if root.endswith(API_PATH):
        raise ValueError(f"base_url is the instance's URL; leave out {API_PATH}, which the client adds")
    return root + API_PATH


def _settings(
    token: str | None,
    base_url: str,
    username: str | None,
    password: str | None,
    otp: str | None,
    sudo: str | None,
    credentials: Credentials | None,
    user_agent: str | None,
    timeout: float,
    max_retries: int,
    retry_base_delay: float,
    rate_limit_wait: float,
    max_retry_wait: float,
) -> Settings:
    headers = {"Accept": "application/json"}
    if user_agent:
        headers["User-Agent"] = user_agent
    return Settings(
        base_url=_api_url(base_url),
        credentials=_credentials(token, username, password, otp, sudo, credentials),
        headers=headers,
        to_error=to_error,
        logger=logger,
        timeout=timeout,
        max_retries=max_retries,
        retry_base_delay=retry_base_delay,
        rate_limit_wait=rate_limit_wait,
        max_retry_wait=max_retry_wait,
    )


class GiteaClient(Resources):
    """Synchronous client.

    Args:
        token: An access token, sent as `Authorization: token <token>`. Pass this, or `username` and `password`,
            or `credentials`.
        base_url: Your Gitea instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for
            an instance under a sub-path. There is no default. The client adds `/api/v1`.
        username: Your username, for Basic authentication with `password`.
        password: Your password, for Basic authentication.
        otp: A current one-time password, sent as `X-GITEA-OTP` with Basic authentication, when your account
            has two-factor authentication on.
        sudo: A user to act as, sent as `Sudo`. Needs an admin's credentials.
        credentials: A provider that sets each request's credentials, instead of the others.
        user_agent: Sent as `User-Agent`, when given.
        timeout: Seconds allowed for each attempt, including reading the whole response.
        max_retries: Retries after the first attempt.
        retry_base_delay: Base in seconds of the exponential backoff.
        rate_limit_wait: Seconds to wait after a 429 with no usable `Retry-After`.
        max_retry_wait: The longest `Retry-After` to wait for, in seconds. A longer one raises
            `RateLimitedError` at once, with the header in `retry_after`.
        http_transport: An httpx transport to use instead of the network.

    The token, password and one-time password are never stored beyond this client, and never logged.
    """

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str,
        username: str | None = None,
        password: str | None = None,
        otp: str | None = None,
        sudo: str | None = None,
        credentials: Credentials | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.BaseTransport | None = None,
    ) -> None:
        settings = _settings(
            token,
            base_url,
            username,
            password,
            otp,
            sudo,
            credentials,
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        self._transport = SyncTransport(settings, http_transport)
        super().__init__(self._transport)

    def close(self) -> None:
        self._transport.http.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncGiteaClient(AsyncResources):
    """Asynchronous client. Takes the same arguments as `GiteaClient`."""

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str,
        username: str | None = None,
        password: str | None = None,
        otp: str | None = None,
        sudo: str | None = None,
        credentials: Credentials | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        settings = _settings(
            token,
            base_url,
            username,
            password,
            otp,
            sudo,
            credentials,
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        self._transport = AsyncTransport(settings, http_transport)
        super().__init__(self._transport)

    async def aclose(self) -> None:
        await self._transport.http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()
