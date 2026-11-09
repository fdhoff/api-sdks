from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import pytest

from mercury_banking import SIGNATURE_HEADER, WebhookSignatureError, verify_webhook

ROOT = Path(__file__).resolve().parents[5]
MERCURY = json.loads((ROOT / "apis/mercury/conformance/webhooks/mercury-signature.json").read_text("utf-8"))
SHARED = json.loads((ROOT / "toolchain/conformance/fixtures/webhooks/hmac-sha256.json").read_text("utf-8"))
VECTORS = [(MERCURY, case) for case in MERCURY["cases"]] + [(SHARED, case) for case in SHARED["cases"]]


def test_the_header_is_the_one_mercury_sends() -> None:
    assert SIGNATURE_HEADER == MERCURY["header_name"] == "Mercury-Signature"


@pytest.mark.parametrize(("vectors", "case"), VECTORS, ids=lambda value: value.get("name", ""))
def test_vector(vectors: dict[str, Any], case: dict[str, Any]) -> None:
    secret = vectors["secret"]

    def verify() -> None:
        tolerance = float(case.get("tolerance", 300))
        verify_webhook(case["body"].encode(), case["header"], secret, tolerance=tolerance, now=case["now"])

    if case["error"] is None:
        verify()
        return
    with pytest.raises(WebhookSignatureError) as caught:
        verify()
    assert caught.value.reason == case["error"]
    assert secret not in str(caught.value)
    assert case["body"] not in str(caught.value)


@pytest.mark.parametrize("tolerance", [0.0, -1.0, math.nan, math.inf])
def test_an_invalid_tolerance_is_rejected(tolerance: float) -> None:
    case = MERCURY["cases"][0]
    with pytest.raises(WebhookSignatureError) as caught:
        verify_webhook(case["body"].encode(), case["header"], MERCURY["secret"], tolerance=tolerance, now=case["now"])
    assert caught.value.reason == "invalid_tolerance"


def test_a_missing_header_is_malformed() -> None:
    with pytest.raises(WebhookSignatureError) as caught:
        verify_webhook(b"{}", None, MERCURY["secret"])
    assert caught.value.reason == "malformed_header"
