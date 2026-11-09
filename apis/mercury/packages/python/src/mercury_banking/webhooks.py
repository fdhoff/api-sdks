"""Checks that a webhook came from Mercury. Mercury's sandbox sends no webhooks, so this is the way to test a handler."""

from __future__ import annotations

from ._runtime import DEFAULT_WEBHOOK_TOLERANCE, WebhookFailure, WebhookSignatureError, verify_webhook

SIGNATURE_HEADER = "Mercury-Signature"
"""The request header that carries a webhook's signature."""

__all__ = ["DEFAULT_WEBHOOK_TOLERANCE", "SIGNATURE_HEADER", "WebhookFailure", "WebhookSignatureError", "verify_webhook"]
