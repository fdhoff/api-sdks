# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from backmarket_seller.api import backbox_api
from backmarket_seller.api import buyback_api
from backmarket_seller.api import care_api
from backmarket_seller.api import categories_api
from backmarket_seller.api import listings_api
from backmarket_seller.api import orders_api
from backmarket_seller.api import shipping_api
from backmarket_seller.api import tasks_api
from backmarket_seller._runtime import AsyncTransport, Operation, SyncTransport

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        backbox_api.OPERATIONS,
        buyback_api.OPERATIONS,
        care_api.OPERATIONS,
        categories_api.OPERATIONS,
        listings_api.OPERATIONS,
        orders_api.OPERATIONS,
        shipping_api.OPERATIONS,
        tasks_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.backbox = backbox_api.BackboxApi(transport)
        self.buyback = buyback_api.BuybackApi(transport)
        self.care = care_api.CareApi(transport)
        self.categories = categories_api.CategoriesApi(transport)
        self.listings = listings_api.ListingsApi(transport)
        self.orders = orders_api.OrdersApi(transport)
        self.shipping = shipping_api.ShippingApi(transport)
        self.tasks = tasks_api.TasksApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.backbox = backbox_api.AsyncBackboxApi(transport)
        self.buyback = buyback_api.AsyncBuybackApi(transport)
        self.care = care_api.AsyncCareApi(transport)
        self.categories = categories_api.AsyncCategoriesApi(transport)
        self.listings = listings_api.AsyncListingsApi(transport)
        self.orders = orders_api.AsyncOrdersApi(transport)
        self.shipping = shipping_api.AsyncShippingApi(transport)
        self.tasks = tasks_api.AsyncTasksApi(transport)
