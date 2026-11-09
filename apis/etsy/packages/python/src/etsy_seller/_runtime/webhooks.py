"""Verification of timestamped HMAC-SHA256 webhook signatures: a header of `t=<unix seconds>,v1=<hex>`, signed over
`<t>.<raw body>` with the endpoint's secret."""

from __future__ import annotations

import hashlib
import hmac
import re
import time
from typing import Literal

DEFAULT_WEBHOOK_TOLERANCE = 300.0

WebhookFailure = Literal["malformed_header", "too_old", "bad_signature"]

_TIMESTAMP = re.compile(r"[0-9]{1,12}")
_SIGNATURE = re.compile(r"[0-9a-fA-F]{64}")
_MESSAGES: dict[WebhookFailure, str] = {
    "malformed_header": "The webhook signature header is malformed",
    "too_old": "The webhook timestamp is older than the tolerance",
    "bad_signature": "No webhook signature matches the body",
}


class WebhookSignatureError(Exception):
    """A webhook failed verification. `reason` says why; the message never holds the secret or the body."""

    def __init__(self, reason: WebhookFailure) -> None:
        super().__init__(_MESSAGES[reason])
        self.reason: WebhookFailure = reason


def _parse(header: str | None) -> tuple[str, list[str]]:
    if header is None:
        raise WebhookSignatureError("malformed_header")
    timestamp: str | None = None
    signatures: list[str] = []
    for entry in header.split(","):
        key, sep, value = entry.strip(" \t").partition("=")
        if not sep:
            raise WebhookSignatureError("malformed_header")
        if key == "t":
            if timestamp is not None or not _TIMESTAMP.fullmatch(value):
                raise WebhookSignatureError("malformed_header")
            timestamp = value
        elif key == "v1":
            signatures.append(value)
    if timestamp is None or not signatures:
        raise WebhookSignatureError("malformed_header")
    return timestamp, signatures


def verify_webhook(
    payload: bytes,
    header: str | None,
    secret: str | bytes,
    *,
    tolerance: float = DEFAULT_WEBHOOK_TOLERANCE,
    now: float | None = None,
) -> None:
    """Checks a webhook's signature header against its raw body, as received and never re-serialised.

    `tolerance` is the oldest timestamp to accept, in seconds, and `now` the time in Unix seconds, by default the
    clock. Any one matching `v1` value is enough, so a header may carry several while a secret rotates. Raises
    `WebhookSignatureError`.
    """
    if tolerance <= 0:
        raise ValueError("The webhook tolerance must be positive")
    timestamp, signatures = _parse(header)
    key = secret.encode() if isinstance(secret, str) else secret
    expected = hmac.new(key, timestamp.encode() + b"." + payload, hashlib.sha256).digest()
    matched = False
    for signature in signatures:
        if _SIGNATURE.fullmatch(signature):
            matched |= hmac.compare_digest(bytes.fromhex(signature), expected)
    if not matched:
        raise WebhookSignatureError("bad_signature")
    if (time.time() if now is None else now) - int(timestamp) > tolerance:
        raise WebhookSignatureError("too_old")
