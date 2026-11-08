# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.fulfillment.api import orders_api, payment_disputes_api, shipping_fulfillments_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        orders_api.OPERATIONS,
        payment_disputes_api.OPERATIONS,
        shipping_fulfillments_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.orders = orders_api.OrdersApi(transport)
        self.payment_disputes = payment_disputes_api.PaymentDisputesApi(transport)
        self.shipping_fulfillments = shipping_fulfillments_api.ShippingFulfillmentsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.orders = orders_api.AsyncOrdersApi(transport)
        self.payment_disputes = payment_disputes_api.AsyncPaymentDisputesApi(transport)
        self.shipping_fulfillments = shipping_fulfillments_api.AsyncShippingFulfillmentsApi(transport)
