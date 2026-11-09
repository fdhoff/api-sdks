"""HTTP message signatures (RFC 9421) with a `Content-Digest` (RFC 9530).

Signing needs the `cryptography` package, which only an API that signs lists as a dependency, so it is
imported when a signer is made.
"""

from __future__ import annotations

import base64
import hashlib
import re
import time
from collections.abc import Callable, Sequence
from urllib.parse import SplitResult, urlsplit

from .credentials import AuthRequest

ED25519 = "ed25519"
RSA_V1_5_SHA256 = "rsa-v1_5-sha256"

_DERIVED = ("@method", "@target-uri", "@authority", "@scheme", "@request-target", "@path", "@query")
_FIELD = re.compile(r"[a-z0-9!#$%&'*+.^_`|~-]+")
_LABEL = re.compile(r"[a-z*][a-z0-9_.*-]*")
_DEFAULT_PORTS = {"http": ":80", "https": ":443"}
# httpx sends `Content-Length: 0` for these methods without a body.
_EMPTY_BODY_LENGTH = ("POST", "PUT", "PATCH")
# A shorter last line of a key's base64 body is too common a string to redact.
_MIN_SECRET_LINE = 16


def content_digest(body: bytes) -> str:
    """The `Content-Digest` value for these exact bytes."""
    return f"sha-256=:{base64.b64encode(hashlib.sha256(body).digest()).decode()}:"


def _pem_lines(pem: str) -> list[str]:
    return [line.strip() for line in pem.strip().splitlines()[1:-1]]


def _authority(url: SplitResult) -> str:
    scheme = url.scheme.lower()
    return url.netloc.rpartition("@")[2].lower().removesuffix(_DEFAULT_PORTS.get(scheme, ""))


def _load_key(pem: str) -> tuple[str, Callable[[bytes], bytes]]:
    from cryptography.exceptions import UnsupportedAlgorithm
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ed25519, padding, rsa

    if not pem.lstrip().startswith("-----BEGIN PRIVATE KEY-----"):
        raise ValueError("The signing key must be an unencrypted PKCS #8 PEM private key")
    try:
        key = serialization.load_pem_private_key(pem.encode(), password=None)
    except UnsupportedAlgorithm:
        raise ValueError("The signing key must be Ed25519 or RSA") from None
    except (ValueError, TypeError):
        raise ValueError("The signing key is not a valid private key") from None
    if isinstance(key, ed25519.Ed25519PrivateKey):
        return ED25519, key.sign
    if isinstance(key, rsa.RSAPrivateKey):
        rsa_key = key
        return RSA_V1_5_SHA256, lambda data: rsa_key.sign(data, padding.PKCS1v15(), hashes.SHA256())
    raise ValueError("The signing key must be Ed25519 or RSA")


def _quote(value: str) -> str:
    if not all(" " <= char <= "~" for char in value):
        raise ValueError("A signature parameter must be printable ASCII")
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _content_length(request: AuthRequest) -> str | None:
    """What httpx sends: the body's length, or `0` for a POST, PUT or PATCH without a body."""
    if request.body:
        return str(len(request.body))
    return "0" if request.method.upper() in _EMPTY_BODY_LENGTH else None


class MessageSigner:
    """Signs each attempt's request: a `Content-Digest` of the body when there is one, then `Signature-Input`
    and `Signature` over `components`, with a fresh `created` time.

    `components` are lowercase field names and the derived components `@method`, `@target-uri`,
    `@authority`, `@scheme`, `@request-target`, `@path` and `@query`. `content-digest` is left out of a
    request with no body. A request without `content-length` or `host` uses the body's length, `0` for a
    POST, PUT or PATCH without one, or the URL's authority, which httpx sends; any other field the request
    lacks is an error. The key is an unencrypted PKCS #8 PEM Ed25519 or RSA private key, and is a secret. `lifetime` is whole seconds.
    """

    def __init__(
        self,
        private_key: str,
        components: Sequence[str],
        *,
        label: str = "sig1",
        key_id: str | None = None,
        include_alg: bool = False,
        lifetime: int | None = None,
        clock: Callable[[], float] = time.time,
    ) -> None:
        for component in components:
            if component.startswith("@") and component not in _DERIVED:
                raise ValueError(f"Unsupported derived component {component}")
            if not component.startswith("@") and not _FIELD.fullmatch(component):
                raise ValueError(f"A covered field must be a lowercase field name: {component}")
        if not _LABEL.fullmatch(label):
            raise ValueError("The signature label must be a lowercase key")
        if lifetime is not None and (type(lifetime) is not int or lifetime < 1):
            raise ValueError("The signature lifetime must be a whole number of seconds, at least 1")
        self.algorithm, self._sign = _load_key(private_key)
        lines = _pem_lines(private_key)
        long_lines = [line for line in lines if len(line) >= _MIN_SECRET_LINE]
        self._secrets = tuple(dict.fromkeys((private_key.strip(), "".join(lines), *long_lines)))
        self._components = tuple(components)
        self._label = label
        self._extra = (f";keyid={_quote(key_id)}" if key_id is not None else "") + (
            f';alg="{self.algorithm}"' if include_alg else ""
        )
        self._lifetime = lifetime
        self._clock = clock

    def __repr__(self) -> str:
        return f"MessageSigner({self.algorithm}, ***)"

    def secrets(self) -> tuple[str, ...]:
        """The private key as given, as its PEM body and as each line of that body, to redact."""
        return self._secrets

    def sign(self, request: AuthRequest) -> None:
        if request.body:
            request.headers["Content-Digest"] = content_digest(request.body)
        components = [
            name for name in self._components if name != "content-digest" or "content-digest" in request.headers
        ]
        created = int(self._clock())
        params = "(" + " ".join(f'"{name}"' for name in components) + f");created={created}{self._extra}"
        if self._lifetime is not None:
            params += f";expires={created + self._lifetime}"
        lines = [f'"{name}": {self._value(request, name)}' for name in components]
        lines.append(f'"@signature-params": {params}')
        signature = base64.b64encode(self._sign("\n".join(lines).encode())).decode()
        request.headers["Signature-Input"] = f"{self._label}={params}"
        request.headers["Signature"] = f"{self._label}=:{signature}:"

    @staticmethod
    def _value(request: AuthRequest, name: str) -> str:
        url = urlsplit(request.url)
        if not name.startswith("@"):
            value = request.headers.get(name)
            if value is None and name == "content-length":
                value = _content_length(request)
            if value is None and name == "host":
                value = _authority(url)
            if value is None:
                raise ValueError(f"The request has no {name} field to sign")
            return value.strip()
        path = url.path or "/"
        query = f"?{url.query}"
        return {
            "@method": request.method.upper(),
            "@target-uri": request.url,
            "@authority": _authority(url),
            "@scheme": url.scheme.lower(),
            "@request-target": path + (query if url.query else ""),
            "@path": path,
            "@query": query,
        }[name]
