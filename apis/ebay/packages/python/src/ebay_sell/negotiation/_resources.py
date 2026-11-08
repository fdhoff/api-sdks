# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.negotiation.api import offers_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation for operations in (offers_api.OPERATIONS,) for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.offers = offers_api.OffersApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.offers = offers_api.AsyncOffersApi(transport)
