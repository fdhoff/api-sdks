"""Signatures for the calls eBay requires EU- and UK-domiciled sellers to sign."""

from __future__ import annotations

from dataclasses import dataclass, field

from ._runtime import MessageSigner

COMPONENTS = ("content-digest", "x-ebay-signature-key", "@method", "@path", "@authority")
_PEM_HEADER = "-----BEGIN PRIVATE KEY-----"


@dataclass(frozen=True)
class SigningKey:
    """A key pair from the Key Management API's `createSigningKey`: its private key, as that call returns it or
    as a PKCS #8 PEM, and its `jwe`, which is sent as `x-ebay-signature-key`. The private key is a secret, and
    eBay returns it only once. Signing needs the `cryptography` package: install `ebay-sell[signing]`."""

    private_key: str = field(repr=False)
    jwe: str

    def signer(self) -> MessageSigner:
        return MessageSigner(_pem(self.private_key), COMPONENTS)


def _pem(private_key: str) -> str:
    """eBay returns the base64 body of the key without the PEM lines around it."""
    key = private_key.strip()
    if key.startswith(_PEM_HEADER):
        return key
    body = "".join(key.split())
    lines = [body[start : start + 64] for start in range(0, len(body), 64)]
    return "\n".join([_PEM_HEADER, *lines, "-----END PRIVATE KEY-----"])


__all__ = ["COMPONENTS", "SigningKey"]
