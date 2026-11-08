# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.developer_analytics.api import rate_limits_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation for operations in (rate_limits_api.OPERATIONS,) for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.rate_limits = rate_limits_api.RateLimitsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.rate_limits = rate_limits_api.AsyncRateLimitsApi(transport)
