from __future__ import annotations

import asyncio
import logging
import time
from collections.abc import AsyncIterator, Callable, Iterator
from typing import Any

import httpx
import pytest

from backmarket_seller._runtime import (
    ApiConnectionError,
    ApiTimeoutError,
    AsyncResource,
    AsyncTransport,
    AuthRequest,
    Credentials,
    Operation,
    Param,
    Resource,
    Scheme,
    Settings,
    SyncTransport,
)
from backmarket_seller.errors import NotFoundError, RateLimitedError, to_error

# Not valid UTF-8, so a body decoded as text cannot come back unchanged.
PDF = bytes([0x25, 0x50, 0x44, 0x46, 0x00, 0xFF, 0xFE, 0x80, 0x0A, 0xC3, 0x28])
SECRET = "synthetic-secret"

DOWNLOAD: Operation[None] = Operation(
    id="download-file",
    method="GET",
    path="/files/{id}",
    resource="files",
    name="download",
    params=(Param("id", "id", "path"),),
    binary_response=True,
    security=((Scheme("token", ()),),),
)
UPLOAD: Operation[Any] = Operation(
    id="upload-file",
    method="POST",
    path="/files",
    resource="files",
    name="upload",
    response=dict[str, Any],
    returns_json=True,
    raw_body="application/octet-stream",
    security=((Scheme("token", ()),),),
)
REPORT: Operation[str] = Operation(
    id="get-report", method="GET", path="/report", resource="reports", name="get", response=str
)


class Recorder(Credentials):
    def __init__(self) -> None:
        self.seen: list[AuthRequest] = []

    def apply(self, request: AuthRequest) -> None:
        self.seen.append(request)
        request.headers["Authorization"] = f"Bearer {SECRET}"

    def secrets(self) -> list[str]:
        return [SECRET]


def settings(credentials: Credentials, **options: Any) -> Settings:
    return Settings(
        base_url="http://api.invalid",
        credentials=credentials,
        headers={"User-Agent": "test"},
        to_error=to_error,
        logger=logging.getLogger("binary-test"),
        max_retries=1,
        rate_limit_wait=0,
        **options,
    )


def resource(
    handler: Callable[[httpx.Request], httpx.Response], **options: Any
) -> tuple[Resource, list[httpx.Request], Recorder]:
    sent: list[httpx.Request] = []
    credentials = Recorder()

    def record(request: httpx.Request) -> httpx.Response:
        request.read()
        sent.append(request)
        return handler(request)

    transport = SyncTransport(settings(credentials, **options), httpx.MockTransport(record))
    return Resource(transport), sent, credentials


def async_resource(
    handler: Callable[[httpx.Request], httpx.Response], **options: Any
) -> tuple[AsyncResource, list[httpx.Request]]:
    sent: list[httpx.Request] = []

    async def record(request: httpx.Request) -> httpx.Response:
        await request.aread()
        sent.append(request)
        return handler(request)

    transport = AsyncTransport(settings(Recorder(), **options), httpx.MockTransport(record))
    return AsyncResource(transport), sent


def pdf(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, headers={"Content-Type": "application/pdf"}, content=PDF)


class Chunks(httpx.SyncByteStream, httpx.AsyncByteStream):
    """A body that arrives in pieces, each `delay` seconds after the last."""

    def __init__(self, chunks: list[bytes], delay: float = 0) -> None:
        self.chunks = chunks
        self.delay = delay
        self.served = 0

    def __iter__(self) -> Iterator[bytes]:
        for chunk in self.chunks:
            time.sleep(self.delay)
            self.served += 1
            yield chunk

    async def __aiter__(self) -> AsyncIterator[bytes]:
        for chunk in self.chunks:
            await asyncio.sleep(self.delay)
            self.served += 1
            yield chunk


def test_a_download_gives_back_the_exact_bytes_and_content_type() -> None:
    client, sent, _ = resource(pdf)
    with client._download(DOWNLOAD, id=7) as download:
        assert download.content_type == "application/pdf"
        assert download.read() == PDF
    assert str(sent[0].url) == "http://api.invalid/files/7"
    assert sent[0].headers["Accept-Encoding"] == "identity"


def test_a_download_streams_chunks_as_they_arrive() -> None:
    stream = Chunks([b"\x00\xff", b"\xfe"])
    client, _, _ = resource(lambda request: httpx.Response(200, stream=stream))
    chunks = client._download(DOWNLOAD, id=1).iter_bytes()
    assert next(chunks) == b"\x00\xff"
    assert stream.served == 1
    assert list(chunks) == [b"\xfe"]


def test_an_empty_download_is_empty_not_an_error() -> None:
    client, _, _ = resource(lambda request: httpx.Response(200))
    download = client._download(DOWNLOAD, id=1)
    assert download.content_type == ""
    assert download.read() == b""


def test_the_deadline_keeps_running_while_a_download_is_read() -> None:
    stream = Chunks([b"a", b"b", b"c"], delay=0.2)
    client, _, _ = resource(lambda request: httpx.Response(200, stream=stream), timeout=0.3)
    with pytest.raises(ApiTimeoutError):
        client._download(DOWNLOAD, id=1).read()


def test_a_download_that_drops_mid_body_is_a_connection_error() -> None:
    class Dropped(httpx.SyncByteStream):
        def __iter__(self) -> Iterator[bytes]:
            yield b"\x00"
            raise httpx.ReadError("dropped")

    client, _, _ = resource(lambda request: httpx.Response(200, stream=Dropped()))
    with pytest.raises(ApiConnectionError):
        client._download(DOWNLOAD, id=1).read()


def test_a_failed_download_is_a_typed_error_with_redacted_text() -> None:
    def missing(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"message": f"no file for {SECRET}"})

    client, _, _ = resource(missing)
    with pytest.raises(NotFoundError) as raised:
        client._download(DOWNLOAD, id=1)
    assert raised.value.raw_body is not None
    assert SECRET not in raised.value.raw_body
    assert "no file" in raised.value.raw_body


def test_a_download_is_retried_until_it_is_returned() -> None:
    replies = iter([httpx.Response(503), pdf(httpx.Request("GET", "http://api.invalid"))])
    client, sent, _ = resource(lambda request: next(replies), retry_base_delay=0)
    assert client._download(DOWNLOAD, id=1).read() == PDF
    assert len(sent) == 2


def test_raw_bytes_are_sent_unchanged_with_the_declared_type_and_retried() -> None:
    replies = iter([httpx.Response(429), httpx.Response(200, json={"id": 1})])
    client, sent, credentials = resource(lambda request: next(replies))
    assert client._call(UPLOAD, _body=PDF) == {"id": 1}
    assert [request.content for request in sent] == [PDF, PDF]
    assert sent[0].headers["Content-Type"] == "application/octet-stream"
    assert credentials.seen[0].body == PDF


def test_a_raw_stream_is_sent_once_and_not_resent_after_a_rate_limit() -> None:
    client, sent, credentials = resource(lambda request: httpx.Response(429))
    with pytest.raises(RateLimitedError):
        client._call(UPLOAD, _body=iter([PDF[:4], PDF[4:]]))
    assert [request.content for request in sent] == [PDF]
    assert credentials.seen[0].body == b""


def test_a_text_response_that_is_not_json_is_text() -> None:
    def report(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"Content-Type": "text/tab-separated-values"}, text="id\tname\n1\tx\n")

    client, sent, _ = resource(report)
    assert client._call(REPORT) == "id\tname\n1\tx\n"
    assert sent[0].headers["Accept-Encoding"] == "gzip"


def test_the_asynchronous_client_downloads_and_uploads_bytes_the_same_way() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "POST":
            return httpx.Response(200, json={"size": len(request.content)})
        return pdf(request)

    client, sent = async_resource(handler)

    async def run() -> None:
        async with await client._download(DOWNLOAD, id=1) as download:
            assert download.content_type == "application/pdf"
            assert b"".join([chunk async for chunk in download.aiter_bytes()]) == PDF
        assert await client._call(UPLOAD, _body=PDF) == {"size": len(PDF)}
        assert await client._call(UPLOAD, _body=iter([PDF[:2], PDF[2:]])) == {"size": len(PDF)}

    asyncio.run(run())
    assert sent[0].headers["Accept-Encoding"] == "identity"
    assert [request.content for request in sent[1:]] == [PDF, PDF]
    assert sent[1].headers["Content-Type"] == "application/octet-stream"


def test_the_asynchronous_deadline_keeps_running_while_a_download_is_read() -> None:
    stream = Chunks([b"a", b"b", b"c"], delay=0.2)
    client, _ = async_resource(lambda request: httpx.Response(200, stream=stream), timeout=0.3)

    async def run() -> None:
        download = await client._download(DOWNLOAD, id=1)
        with pytest.raises(ApiTimeoutError):
            await download.aread()

    asyncio.run(run())


def test_the_asynchronous_client_does_not_resend_a_stream() -> None:
    client, sent = async_resource(lambda request: httpx.Response(429))

    async def run() -> None:
        with pytest.raises(RateLimitedError):
            await client._call(UPLOAD, _body=iter([PDF]))

    asyncio.run(run())
    assert len(sent) == 1
