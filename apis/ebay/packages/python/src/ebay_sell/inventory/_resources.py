# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.inventory.api import (
    inventory_item_groups_api,
    inventory_items_api,
    listings_api,
    locations_api,
    offers_api,
    product_compatibility_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        inventory_item_groups_api.OPERATIONS,
        inventory_items_api.OPERATIONS,
        listings_api.OPERATIONS,
        locations_api.OPERATIONS,
        offers_api.OPERATIONS,
        product_compatibility_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.inventory_item_groups = inventory_item_groups_api.InventoryItemGroupsApi(transport)
        self.inventory_items = inventory_items_api.InventoryItemsApi(transport)
        self.listings = listings_api.ListingsApi(transport)
        self.locations = locations_api.LocationsApi(transport)
        self.offers = offers_api.OffersApi(transport)
        self.product_compatibility = product_compatibility_api.ProductCompatibilityApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.inventory_item_groups = inventory_item_groups_api.AsyncInventoryItemGroupsApi(transport)
        self.inventory_items = inventory_items_api.AsyncInventoryItemsApi(transport)
        self.listings = listings_api.AsyncListingsApi(transport)
        self.locations = locations_api.AsyncLocationsApi(transport)
        self.offers = offers_api.AsyncOffersApi(transport)
        self.product_compatibility = product_compatibility_api.AsyncProductCompatibilityApi(transport)
