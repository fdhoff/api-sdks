from __future__ import annotations

import base64
import itertools
import logging
from collections.abc import Callable
from typing import Any

import httpx
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519

from backmarket_seller._runtime import (
    ED25519,
    RSA_V1_5_SHA256,
    AuthRequest,
    Credentials,
    MessageSigner,
    Operation,
    Param,
    Resource,
    Scheme,
    Settings,
    SyncTransport,
    content_digest,
    redact,
)
from backmarket_seller.errors import to_error

# The published test keys of RFC 9421, Appendix B.1.4 and B.1.1. The RSA key is re-encoded from PKCS #1 to PKCS #8.
ED25519_KEY = """-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF
-----END PRIVATE KEY-----
"""
RSA_KEY = """-----BEGIN PRIVATE KEY-----
MIIEwgIBADANBgkqhkiG9w0BAQEFAASCBKwwggSoAgEAAoIBAQCEAph22h6jLzNw
BxHzvgvxydnErMAbB3u/foA+ns+/pDaN2w8FGvBYQGd7Pp3RQMoPAZtzqfF8RcDL
mZuGBqPOvDcw4S3y4Dm3FIqhsGkoN4Es6x0koWowaZcJC8Qbth6ZzENNE/ECV4gC
BhhGNNJ39AHBVb07A0WF6SujdG2WKdXRrvmN9mCSd79iKS1K8sbfiXDbOpcENMLk
0dE5SoZOUwvg+U1lLlGLZThoI3HatQ9FwoiUTQ+4rEjhP4choWm/z6t1Xp5SA6sH
bF4jV1IUWf+ee/k6hkkQgH5Wa4qfcMJRwJlIWVA9JdJ8EOJQaHA7Dvpa5JKx/UPh
v+8ugnXTAgMBAAECggEAb8lm5JZ2hUduLnq+OAKCSODeWQ7Uqs7eet2bqeuAD0/2
po+PG4qhZoo7VwFCUTWlJan9wqdxiAPlbEQKkCdFRcbakbjN2TMJjMCHWL5zfgvq
hmgeyKsrqg1wSce97J1/Mkvn3fh6CbqnwNb6bVFDvTJS3i5FzRhKiv6rUsYm8ZAd
F4XRaYkFkeuHPl7rc+ruUTSAjC4GovxIxoDJFe0r4kbFmkiZOr40e8RZYK7T1IKr
Svzfxx5AjnlK/OZOTCq0L7wBPbMW+IxmQpFCjpI+yuoi3FlZG3LaLNrBMXQF/lLZ
UDHs77q3fAGxDWwum2hKBfdBuUQtjlqwjQlgXPsskQKBiQCyp5QmapcTcs/y1igi
MwgAqJOb2jqmw+VzwKssj0IfRRu5oDYkI4xwI2rxLJhtOqCdaUH1l9wCb9wWkDy1
hyL2bm9grwc3FCv7wVLdCjw31Enx3RTkKzAPMxh9GCEB9QbCaVaPmGnWlDMC6HBs
5cW3EodWww+HPUgG0X1jyO+CqBgctubKK7WbAnkAvSlgXQbvHzWmuUBFRHAejRh/
naQTDV3GnH4lcRHuFBFZCSLn82xQS2/7xFOqfabqq17kNcvKfzdvWpGxxJ2cILAq
0pZS6DmrZlvBU4IkK2ZHCac/XfWVZFh+PrsH/EnVkDpfcYR/iw1F40C1q5w8R6WB
Haew3SApAoGIaiodZsrWpi8HFfZfeRs8OS/0L5x6WBl3Y9btoZgsIeruc9uZ8NXT
IdxaM6FdnyNEyOYA1VH94tDYR+xEt1br1ud/dkPslLV/Aac7d7EaYc7cdkb7oC9t
6sphVg0dqE0UTDlOwBxBYMtGmQbJsFzGpmjzVgKqWqJ3B947li2U7t63HXEvKprY
2wJ4b0DzpSMb5p42dcQgOTU8Mr4S6JOEhRr/YjErMkpaXUEqvZ3jEB9HRmcRi5Gt
t4NBiBMiY6V9br8a5gjEpiAQoIUcWokBMAYjEeurU8M6JLBd3YaZVVjISaFmdtyn
wLFoQxCh6/EC1rSywwrfDpSwO29S9i8XbaapAoGIPkbARLOwU/LcZrQy9mmfcPoQ
lAuCyeu1Q9nH7PYSnbHTFzmiud4Hl8bIXU9a0/58blDoOl3PctF+b4rAEJYUpCOD
u5PFyN6uEFYRg+YQwpjBMkXk8Eb39128ctARB40Lx8caDhRdTyaEedIG3cQDXSpA
l9EOzXkzfx4bZxjAHU9mkMdJwOcMDQ==
-----END PRIVATE KEY-----
"""
RFC_BODY = b'{"hello": "world"}'
COVERED = ["content-digest", "@method", "@path", "@authority"]

UPLOAD: Operation[Any] = Operation(
    id="upload",
    method="POST",
    path="/files",
    resource="files",
    name="upload",
    params=(Param("file", "file", "form"),),
    response=dict[str, Any],
    security=((Scheme("key"),),),
)

LIST: Operation[Any] = Operation(
    id="list",
    method="GET",
    path="/files",
    resource="files",
    name="list",
    response=dict[str, Any],
    security=((Scheme("key"),),),
)


def auth_request(method: str, url: str, headers: dict[str, str], body: bytes) -> AuthRequest:
    return AuthRequest(method, url, httpx.Headers(headers), body, UPLOAD)


def fresh_key() -> tuple[str, ed25519.Ed25519PublicKey]:
    key = ed25519.Ed25519PrivateKey.generate()
    pem = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
    return pem.decode(), key.public_key()


class Signed(Credentials):
    def __init__(self, signer: MessageSigner) -> None:
        self.signer = signer

    def apply(self, request: AuthRequest) -> None:
        request.headers["Authorization"] = "Bearer synthetic-token"
        self.signer.sign(request)

    def secrets(self) -> list[str]:
        return ["synthetic-token", *self.signer.secrets()]


def resource(credentials: Credentials, handler: Callable[[httpx.Request], httpx.Response]) -> Resource:
    settings = Settings(
        base_url="https://mock.invalid/v1",
        credentials=credentials,
        headers={"User-Agent": "test"},
        to_error=to_error,
        logger=logging.getLogger("signing-test"),
    )
    return Resource(SyncTransport(settings, httpx.MockTransport(handler)))


def verify(public: ed25519.Ed25519PublicKey, request: httpx.Request, components: list[str]) -> None:
    label, params = request.headers["signature-input"].split("=", 1)
    values = {
        "content-digest": request.headers.get("content-digest"),
        "@method": request.method,
        "@path": request.url.path,
        "@authority": request.url.netloc.decode(),
    }
    base = "".join(f'"{name}": {values[name]}\n' for name in components) + f'"@signature-params": {params}'
    signature = request.headers["signature"].removeprefix(f"{label}=:").removesuffix(":")
    public.verify(base64.b64decode(signature), base.encode())


def test_content_digest_matches_rfc_9530() -> None:
    assert content_digest(b'{"hello": "world"}\n') == "sha-256=:RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=:"


def test_ed25519_matches_rfc_9421_appendix_b_2_6() -> None:
    signer = MessageSigner(
        ED25519_KEY,
        ["date", "@method", "@path", "@authority", "content-type", "content-length"],
        label="sig-b26",
        key_id="test-key-ed25519",
        clock=lambda: 1618884473,
    )
    headers = {"Date": "Tue, 20 Apr 2021 02:07:55 GMT", "Content-Type": "application/json", "Content-Length": "18"}
    request = auth_request("POST", "https://example.com/foo?param=Value&Pet=dog", headers, RFC_BODY)
    signer.sign(request)
    assert signer.algorithm == ED25519
    assert request.headers["content-digest"] == content_digest(RFC_BODY)
    assert request.headers["signature-input"] == (
        'sig-b26=("date" "@method" "@path" "@authority" "content-type" "content-length")'
        ';created=1618884473;keyid="test-key-ed25519"'
    )
    assert request.headers["signature"] == (
        "sig-b26=:wqcAqbmYJ2ji2glfAMaRy4gruYYnx2nEFN2HN6jrnDnQCK1u02Gb04v9EDgwUPiu4A0w6vuQv5lIp5WPpBKRCw==:"
    )


def test_rsa_matches_rfc_9421_section_4_3() -> None:
    signer = MessageSigner(
        RSA_KEY,
        ["@method", "@authority", "@path", "content-digest", "content-type", "content-length", "forwarded"],
        label="proxy_sig",
        key_id="test-key-rsa",
        include_alg=True,
        lifetime=60,
        clock=lambda: 1618884480,
    )
    # No body, so the signer keeps the RFC's own SHA-512 digest instead of adding one.
    headers = {
        "Content-Type": "application/json",
        "Content-Length": "18",
        "Forwarded": "for=192.0.2.123;host=example.com;proto=https",
        "Content-Digest": "sha-512=:WZDPaVn/7XgHaAy8pmojAkGWoRx2UFChF41A2svX+TaPm+AbwAgBWnrIiYllu7BNNyealdVLvRwEmTHWXvJwew==:",
    }
    request = auth_request("POST", "https://origin.host.internal.example/foo?param=Value&Pet=dog", headers, b"")
    signer.sign(request)
    assert signer.algorithm == RSA_V1_5_SHA256
    assert request.headers["signature-input"] == (
        'proxy_sig=("@method" "@authority" "@path" "content-digest" "content-type" "content-length" "forwarded")'
        ';created=1618884480;keyid="test-key-rsa";alg="rsa-v1_5-sha256";expires=1618884540'
    )
    assert request.headers["signature"] == (
        "proxy_sig=:S6ZzPXSdAMOPjN/6KXfXWNO/f7V6cHm7BXYUh3YD/fRad4BCaRZxP+JH+8XY1I6+8Cy+CM5g92iHgxtRPz+MjniOaYmdkDcnL9"
        "cCpXJleXsOckpURl49GwiyUpZ10KHgOEe11sx3G2gxI8S0jnxQB+Pu68U9vVcasqOWAEObtNKKZd8tSFu7LB5YAv0RAGhB8tmpv7sFnIm9y+7X5"
        "kXQfi8NMaZaA8i2ZHwpBdg7a6CMfwnnrtflzvZdXAsD3LH2TwevU+/PBPv0B6NMNk93wUs/vfJvye+YuI87HU38lZHowtznbLVdp770I6VHR6Wf"
        "gS9ddzirrswsE1w5o0LV/g==:"
    )


def test_each_attempt_is_signed_again_over_its_own_body() -> None:
    pem, public = fresh_key()
    clock = itertools.count(1700000000)
    signer = MessageSigner(pem, COVERED, clock=lambda: next(clock))
    sent: list[httpx.Request] = []
    replies = iter([httpx.Response(429, headers={"retry-after": "0"}), httpx.Response(200, json={"id": 1})])

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return next(replies)

    assert resource(Signed(signer), handler)._call(UPLOAD, file=b"synthetic") == {"id": 1}
    assert len(sent) == 2
    for created, request in zip((1700000000, 1700000001), sent):
        assert request.headers["content-digest"] == content_digest(request.content)
        assert (
            request.headers["signature-input"]
            == f'sig1=("content-digest" "@method" "@path" "@authority");created={created}'
        )
        verify(public, request, COVERED)


def test_a_request_without_a_body_has_no_digest() -> None:
    pem, public = fresh_key()
    signer = MessageSigner(pem, COVERED, clock=lambda: 1700000000)
    sent: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request)
        return httpx.Response(200, json={"id": 1})

    resource(Signed(signer), handler)._call(LIST)
    assert "content-digest" not in sent[0].headers
    assert sent[0].headers["signature-input"] == 'sig1=("@method" "@path" "@authority");created=1700000000'
    verify(public, sent[0], ["@method", "@path", "@authority"])


def test_rejects_unsupported_keys_and_components() -> None:
    p256 = ec.generate_private_key(ec.SECP256R1()).private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()
    )
    for key, components in [
        (p256.decode(), COVERED),
        ("not a key", COVERED),
        (ED25519_KEY, ["@status"]),
        (ED25519_KEY, ["Content-Type"]),
        (ED25519_KEY, ['"@query-param";name="Pet"']),
    ]:
        with pytest.raises(ValueError):
            MessageSigner(key, components)
    signer = MessageSigner(ED25519_KEY, ["x-missing"])
    with pytest.raises(ValueError, match="x-missing"):
        signer.sign(auth_request("GET", "https://example.com/", {}, b""))


def test_the_private_key_is_a_secret() -> None:
    signer = MessageSigner(ED25519_KEY, COVERED)
    body = "MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF"
    assert body not in repr(signer)
    assert redact(Signed(signer), f"key {ED25519_KEY.strip()} and {body}") == "key *** and ***"
