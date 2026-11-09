from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from backmarket_seller._runtime import WebhookSignatureError, verify_webhook

ROOT = Path(__file__).resolve().parents[5]
VECTORS = json.loads((ROOT / "toolchain/conformance/fixtures/webhooks/hmac-sha256.json").read_text("utf-8"))
SECRET = VECTORS["secret"]


@pytest.mark.parametrize("case", VECTORS["cases"], ids=lambda case: case["name"])
def test_vector(case: dict[str, Any]) -> None:
    def verify() -> None:
        tolerance = float(case.get("tolerance", 300))
        verify_webhook(case["body"].encode(), case["header"], SECRET, tolerance=tolerance, now=case["now"])

    if case["error"] is None:
        verify()
        return
    with pytest.raises(WebhookSignatureError) as caught:
        verify()
    assert caught.value.reason == case["error"]
    assert SECRET not in str(caught.value)
    assert case["body"] not in str(caught.value)


def test_default_tolerance_and_clock() -> None:
    case = VECTORS["cases"][0]
    with pytest.raises(WebhookSignatureError) as caught:
        verify_webhook(case["body"].encode(), case["header"], SECRET)
    assert caught.value.reason == "too_old"


def test_secret_as_bytes() -> None:
    case = VECTORS["cases"][0]
    verify_webhook(case["body"].encode(), case["header"], SECRET.encode(), now=case["now"])


def test_missing_header() -> None:
    with pytest.raises(WebhookSignatureError) as caught:
        verify_webhook(b"{}", None, SECRET)
    assert caught.value.reason == "malformed_header"
