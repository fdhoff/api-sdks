# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.finances.api import (
    billing_activities_api,
    order_earnings_api,
    payouts_api,
    seller_funds_api,
    transactions_api,
    transfers_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        billing_activities_api.OPERATIONS,
        order_earnings_api.OPERATIONS,
        payouts_api.OPERATIONS,
        seller_funds_api.OPERATIONS,
        transactions_api.OPERATIONS,
        transfers_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.billing_activities = billing_activities_api.BillingActivitiesApi(transport)
        self.order_earnings = order_earnings_api.OrderEarningsApi(transport)
        self.payouts = payouts_api.PayoutsApi(transport)
        self.seller_funds = seller_funds_api.SellerFundsApi(transport)
        self.transactions = transactions_api.TransactionsApi(transport)
        self.transfers = transfers_api.TransfersApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.billing_activities = billing_activities_api.AsyncBillingActivitiesApi(transport)
        self.order_earnings = order_earnings_api.AsyncOrderEarningsApi(transport)
        self.payouts = payouts_api.AsyncPayoutsApi(transport)
        self.seller_funds = seller_funds_api.AsyncSellerFundsApi(transport)
        self.transactions = transactions_api.AsyncTransactionsApi(transport)
        self.transfers = transfers_api.AsyncTransfersApi(transport)
