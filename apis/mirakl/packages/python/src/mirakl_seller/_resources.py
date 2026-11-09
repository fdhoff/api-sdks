# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from mirakl_seller._runtime import AsyncTransport, Operation, SyncTransport
from mirakl_seller.api import (
    accounting_api,
    messages_api,
    offers_api,
    orders_api,
    picklists_api,
    platform_api,
    products_api,
    promotions_api,
    returns_api,
    shipments_api,
    shop_api,
    users_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        accounting_api.OPERATIONS,
        messages_api.OPERATIONS,
        offers_api.OPERATIONS,
        orders_api.OPERATIONS,
        picklists_api.OPERATIONS,
        platform_api.OPERATIONS,
        products_api.OPERATIONS,
        promotions_api.OPERATIONS,
        returns_api.OPERATIONS,
        shipments_api.OPERATIONS,
        shop_api.OPERATIONS,
        users_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.accounting = accounting_api.AccountingApi(transport)
        self.messages = messages_api.MessagesApi(transport)
        self.offers = offers_api.OffersApi(transport)
        self.orders = orders_api.OrdersApi(transport)
        self.picklists = picklists_api.PicklistsApi(transport)
        self.platform = platform_api.PlatformApi(transport)
        self.products = products_api.ProductsApi(transport)
        self.promotions = promotions_api.PromotionsApi(transport)
        self.returns = returns_api.ReturnsApi(transport)
        self.shipments = shipments_api.ShipmentsApi(transport)
        self.shop = shop_api.ShopApi(transport)
        self.users = users_api.UsersApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.accounting = accounting_api.AsyncAccountingApi(transport)
        self.messages = messages_api.AsyncMessagesApi(transport)
        self.offers = offers_api.AsyncOffersApi(transport)
        self.orders = orders_api.AsyncOrdersApi(transport)
        self.picklists = picklists_api.AsyncPicklistsApi(transport)
        self.platform = platform_api.AsyncPlatformApi(transport)
        self.products = products_api.AsyncProductsApi(transport)
        self.promotions = promotions_api.AsyncPromotionsApi(transport)
        self.returns = returns_api.AsyncReturnsApi(transport)
        self.shipments = shipments_api.AsyncShipmentsApi(transport)
        self.shop = shop_api.AsyncShopApi(transport)
        self.users = users_api.AsyncUsersApi(transport)
