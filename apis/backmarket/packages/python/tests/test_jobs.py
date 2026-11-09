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
    DecodeError,
    Job,
    JobTimeoutError,
    Operation,
    Param,
    Resource,
    Settings,
    StaticCredentials,
    SyncTransport,
)
from backmarket_seller.errors import to_error

SECRET = "synthetic-secret"
BASE = "https://api.example.test"

# A synthetic start, status and report trio. Only the status operation is polled.
START: Operation[Any] = Operation(
    id="startImport", method="POST", path="/imports", resource="imports", name="start", response=dict[str, Any]
)
STATUS: Operation[Any] = Operation(
    id="getImport",
    method="GET",
    path="/imports/{import_id}",
    resource="imports",
    name="get",
    params=(Param("import_id", "import_id", "path"),),
    response=dict[str, Any],
    returns_json=True,
    job=Job(state="progress.state", done=("COMPLETE",), failed=("FAILED",)),
)
REPORT: Operation[None] = Operation(
    id="getImportReport",
    method="GET",
    path="/imports/{import_id}/report",
    resource="imports",
    name="report",
    params=(Param("import_id", "import_id", "path"),),
    binary_response=True,
)


def settings(**options: Any) -> Settings:
    return Settings(
        base_url=BASE,
        credentials=StaticCredentials({"Authorization": SECRET}, secrets=[SECRET]),
        headers={"User-Agent": "test"},
        to_error=to_error,
        logger=logging.getLogger("jobs-test"),
        max_retries=2,
        rate_limit_wait=0,
        retry_base_delay=0,
        **options,
    )


def status(state: Any) -> httpx.Response:
    return httpx.Response(200, json={"import_id": 7, "progress": {"state": state}})


def replies(*responses: httpx.Response) -> Callable[[httpx.Request], httpx.Response]:
    remaining = iter(responses)
    return lambda request: next(remaining)


def resource(handler: Callable[[httpx.Request], httpx.Response]) -> tuple[Resource, list[httpx.Request]]:
    sent: list[httpx.Request] = []

    def record(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return handler(request)

    return Resource(SyncTransport(settings(), httpx.MockTransport(record))), sent


def async_resource(
    handler: Callable[[httpx.Request], httpx.Response],
) -> tuple[AsyncResource, list[httpx.Request]]:
    sent: list[httpx.Request] = []

    async def record(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return handler(request)

    return AsyncResource(AsyncTransport(settings(), httpx.MockTransport(record))), sent


def test_wait_polls_until_the_job_is_done_and_returns_its_last_status() -> None:
    client, sent = resource(replies(status("WAITING"), status("RUNNING"), status("COMPLETE")))
    result = client._wait(STATUS, interval=0, timeout=5, import_id=7)
    assert result["progress"]["state"] == "COMPLETE"
    assert [str(request.url) for request in sent] == [f"{BASE}/imports/7"] * 3


def test_a_failed_job_returns_its_status_rather_than_raising() -> None:
    client, sent = resource(replies(status("RUNNING"), status("FAILED")))
    assert client._wait(STATUS, interval=0, timeout=5, import_id=7)["progress"]["state"] == "FAILED"
    assert len(sent) == 2


def test_a_job_that_outlasts_the_deadline_is_a_typed_timeout_with_its_last_status() -> None:
    client, sent = resource(lambda request: status("RUNNING"))
    with pytest.raises(JobTimeoutError) as raised:
        client._wait(STATUS, interval=0.02, timeout=0.05, import_id=7)
    assert raised.value.result["progress"]["state"] == "RUNNING"
    assert len(sent) >= 2


def test_a_rate_limit_while_polling_is_retried_after_its_retry_after() -> None:
    limited = httpx.Response(429, headers={"Retry-After": "0"})
    client, sent = resource(replies(status("RUNNING"), limited, status("COMPLETE")))
    assert client._wait(STATUS, interval=0, timeout=5, import_id=7)["progress"]["state"] == "COMPLETE"
    assert len(sent) == 3


def test_a_state_that_is_not_a_string_is_a_decode_error() -> None:
    client, _ = resource(lambda request: status(3))
    with pytest.raises(DecodeError, match="progress.state"):
        client._wait(STATUS, interval=0, timeout=5, import_id=7)


def test_wait_refuses_a_negative_interval_or_timeout_and_an_operation_without_a_job() -> None:
    client, sent = resource(lambda request: status("COMPLETE"))
    with pytest.raises(ValueError, match="interval"):
        client._wait(STATUS, interval=-1, timeout=5, import_id=7)
    with pytest.raises(ValueError, match="timeout"):
        client._wait(STATUS, interval=0, timeout=-1, import_id=7)
    with pytest.raises(ValueError, match="does not report a job"):
        client._wait(START, interval=0, timeout=5)
    assert sent == []


def test_the_asynchronous_wait_polls_the_same_way_and_stops_when_cancelled() -> None:
    client, sent = async_resource(replies(status("WAITING"), status("COMPLETE")))

    async def done() -> None:
        result = await client._wait(STATUS, interval=0, timeout=5, import_id=7)
        assert result["progress"]["state"] == "COMPLETE"

    asyncio.run(done())
    assert len(sent) == 2

    running, polled = async_resource(lambda request: status("RUNNING"))

    async def cancelled() -> None:
        task = asyncio.create_task(running._wait(STATUS, interval=60, timeout=600, import_id=7))
        while not polled:
            await asyncio.sleep(0)
        await asyncio.sleep(0.01)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(cancelled())
    assert len(polled) == 1


def test_the_asynchronous_wait_has_the_same_deadline() -> None:
    client, _ = async_resource(lambda request: status("RUNNING"))

    async def run() -> None:
        with pytest.raises(JobTimeoutError):
            await client._wait(STATUS, interval=0.02, timeout=0.05, import_id=7)

    asyncio.run(run())


def transport(handler: Callable[[httpx.Request], httpx.Response]) -> tuple[SyncTransport, list[httpx.Request]]:
    sent: list[httpx.Request] = []

    def record(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return handler(request)

    return SyncTransport(settings(), httpx.MockTransport(record)), sent


def csv(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, headers={"Content-Type": "text/csv"}, content=b"id;error\n1;none\n")


def redirect(location: str) -> httpx.Response:
    return httpx.Response(302, headers={"Location": location})


def test_a_download_url_on_the_base_origin_sends_credentials() -> None:
    client, sent = transport(csv)
    with client.download_url(f"{BASE}/files/report.csv?sig=abc") as download:
        assert download.content_type == "text/csv"
        assert download.read() == b"id;error\n1;none\n"
    assert sent[0].headers["Authorization"] == SECRET
    assert sent[0].headers["Accept-Encoding"] == "identity"


@pytest.mark.parametrize(
    "url",
    [
        "https://files.example.test/report.csv",
        "http://api.example.test/report.csv",
        "https://api.example.test:8443/report.csv",
    ],
)
def test_a_download_url_on_another_scheme_host_or_port_sends_no_credentials(url: str) -> None:
    client, sent = transport(csv)
    assert client.download_url(url).read() == b"id;error\n1;none\n"
    assert "Authorization" not in sent[0].headers


def test_a_redirect_to_another_origin_drops_credentials_for_the_rest_of_the_chain() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "api.example.test" and request.url.path == "/files/1":
            return redirect("https://files.example.test/signed/1")
        if request.url.host == "files.example.test":
            return redirect(f"{BASE}/files/final")
        return csv(request)

    client, sent = transport(handler)
    assert client.download_url(f"{BASE}/files/1").read() == b"id;error\n1;none\n"
    assert [str(request.url) for request in sent] == [
        f"{BASE}/files/1",
        "https://files.example.test/signed/1",
        f"{BASE}/files/final",
    ]
    assert [request.headers.get("Authorization") for request in sent] == [SECRET, None, None]


def test_a_relative_redirect_on_the_base_origin_keeps_credentials() -> None:
    client, sent = transport(lambda request: redirect("/files/2") if request.url.path == "/files/1" else csv(request))
    client.download_url(f"{BASE}/files/1").read()
    assert [request.headers.get("Authorization") for request in sent] == [SECRET, SECRET]


def test_a_download_url_refuses_a_relative_url_and_endless_redirects() -> None:
    client, sent = transport(lambda request: redirect(str(request.url)))
    with pytest.raises(ValueError, match="absolute"):
        client.download_url("/files/1")
    with pytest.raises(ValueError, match="absolute"):
        client.download_url("ftp://api.example.test/files/1")
    assert sent == []
    with pytest.raises(DecodeError, match="redirects"):
        client.download_url(f"{BASE}/files/1")
    assert len(sent) == 6


def test_the_asynchronous_download_url_drops_credentials_across_origins() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "api.example.test":
            return redirect("https://files.example.test/signed/1")
        return csv(request)

    sent: list[httpx.Request] = []

    async def record(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return handler(request)

    client = AsyncTransport(settings(), httpx.MockTransport(record))

    async def run() -> None:
        async with await client.download_url(f"{BASE}/files/1") as download:
            assert await download.aread() == b"id;error\n1;none\n"

    asyncio.run(run())
    assert [request.headers.get("Authorization") for request in sent] == [SECRET, None]


def test_the_report_of_a_job_is_an_ordinary_download() -> None:
    client, sent = resource(csv)
    assert client._download(REPORT, import_id=7).read() == b"id;error\n1;none\n"
    assert str(sent[0].url) == f"{BASE}/imports/7/report"
