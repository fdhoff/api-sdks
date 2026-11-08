# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.feedback.api import feedback_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation for operations in (feedback_api.OPERATIONS,) for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.feedback = feedback_api.FeedbackApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.feedback = feedback_api.AsyncFeedbackApi(transport)
