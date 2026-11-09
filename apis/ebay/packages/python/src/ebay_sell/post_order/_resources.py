# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.post_order.api import cancellations_api, cases_api, inquiries_api, return_preferences_api, returns_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        cancellations_api.OPERATIONS,
        cases_api.OPERATIONS,
        inquiries_api.OPERATIONS,
        return_preferences_api.OPERATIONS,
        returns_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.cancellations = cancellations_api.CancellationsApi(transport)
        self.cases = cases_api.CasesApi(transport)
        self.inquiries = inquiries_api.InquiriesApi(transport)
        self.return_preferences = return_preferences_api.ReturnPreferencesApi(transport)
        self.returns = returns_api.ReturnsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.cancellations = cancellations_api.AsyncCancellationsApi(transport)
        self.cases = cases_api.AsyncCasesApi(transport)
        self.inquiries = inquiries_api.AsyncInquiriesApi(transport)
        self.return_preferences = return_preferences_api.AsyncReturnPreferencesApi(transport)
        self.returns = returns_api.AsyncReturnsApi(transport)
