# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.inventory import models as _models
from ebay_sell.inventory.models.base_response import BaseResponse
from ebay_sell.inventory.models.bulk_get_inventory_item import BulkGetInventoryItem
from ebay_sell.inventory.models.bulk_get_inventory_item_response import BulkGetInventoryItemResponse
from ebay_sell.inventory.models.bulk_inventory_item import BulkInventoryItem
from ebay_sell.inventory.models.bulk_inventory_item_response import BulkInventoryItemResponse
from ebay_sell.inventory.models.bulk_price_quantity import BulkPriceQuantity
from ebay_sell.inventory.models.bulk_price_quantity_response import BulkPriceQuantityResponse
from ebay_sell.inventory.models.error import Error
from ebay_sell.inventory.models.inventory_item import InventoryItem
from ebay_sell.inventory.models.inventory_item_with_sku_locale_groupid import InventoryItemWithSkuLocaleGroupid
from ebay_sell.inventory.models.inventory_items import InventoryItems

_bulk_create_or_replace_inventory_item: Operation[BulkInventoryItemResponse] = Operation(
    id="bulkCreateOrReplaceInventoryItem",
    method="POST",
    path="/sell/inventory/v1/bulk_create_or_replace_inventory_item",
    resource="inventory_items",
    name="bulk_create_or_replace",
    params=(Param("Content-Language", "content_language", "header"),),
    response=BulkInventoryItemResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_bulk_get_inventory_item: Operation[BulkGetInventoryItemResponse] = Operation(
    id="bulkGetInventoryItem",
    method="POST",
    path="/sell/inventory/v1/bulk_get_inventory_item",
    resource="inventory_items",
    name="bulk_get",
    params=(),
    response=BulkGetInventoryItemResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                ),
            ),
        ),
    ),
    host="api",
)
_bulk_update_price_quantity: Operation[BulkPriceQuantityResponse] = Operation(
    id="bulkUpdatePriceQuantity",
    method="POST",
    path="/sell/inventory/v1/bulk_update_price_quantity",
    resource="inventory_items",
    name="bulk_update_price_quantity",
    params=(),
    response=BulkPriceQuantityResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_create_or_replace_inventory_item: Operation[BaseResponse] = Operation(
    id="createOrReplaceInventoryItem",
    method="PUT",
    path="/sell/inventory/v1/inventory_item/{sku}",
    resource="inventory_items",
    name="create_or_replace",
    params=(
        Param("sku", "sku", "path"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=BaseResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_delete_inventory_item: Operation[Error] = Operation(
    id="deleteInventoryItem",
    method="DELETE",
    path="/sell/inventory/v1/inventory_item/{sku}",
    resource="inventory_items",
    name="delete",
    params=(Param("sku", "sku", "path"),),
    response=Error,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_inventory_item: Operation[InventoryItemWithSkuLocaleGroupid] = Operation(
    id="getInventoryItem",
    method="GET",
    path="/sell/inventory/v1/inventory_item/{sku}",
    resource="inventory_items",
    name="get",
    params=(Param("sku", "sku", "path"),),
    response=InventoryItemWithSkuLocaleGroupid,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                ),
            ),
        ),
    ),
    host="api",
)
_get_inventory_items: Operation[InventoryItems] = Operation(
    id="getInventoryItems",
    method="GET",
    path="/sell/inventory/v1/inventory_item",
    resource="inventory_items",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=InventoryItems,
    returns_json=True,
    iterator="iter",
    item=_models.InventoryItemWithSkuLocaleGroupid,
    paging=NextLink(
        items="inventoryItems",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _bulk_create_or_replace_inventory_item,
    _bulk_get_inventory_item,
    _bulk_update_price_quantity,
    _create_or_replace_inventory_item,
    _delete_inventory_item,
    _get_inventory_item,
    _get_inventory_items,
)


class InventoryItemsApi(Resource):
    @checked
    def bulk_create_or_replace(
        self,
        body: Union[BulkInventoryItem, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BulkInventoryItemResponse:
        """Create or replace several inventory items."""
        return self._call(
            _bulk_create_or_replace_inventory_item,
            _body=body,
            content_language=content_language,
        )

    @checked
    def bulk_get(
        self,
        body: Union[BulkGetInventoryItem, Mapping[str, Any]],
    ) -> BulkGetInventoryItemResponse:
        """Get several inventory items by SKU."""
        return self._call(
            _bulk_get_inventory_item,
            _body=body,
        )

    @checked
    def bulk_update_price_quantity(
        self,
        body: Union[BulkPriceQuantity, Mapping[str, Any]],
    ) -> BulkPriceQuantityResponse:
        """Update the price and quantity of several inventory items and their offers."""
        return self._call(
            _bulk_update_price_quantity,
            _body=body,
        )

    @checked
    def create_or_replace(
        self,
        sku: StrictStr,
        body: Union[InventoryItem, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BaseResponse:
        """Create or replace an inventory item."""
        return self._call(
            _create_or_replace_inventory_item,
            sku=sku,
            _body=body,
            content_language=content_language,
        )

    @checked
    def delete(
        self,
        sku: StrictStr,
    ) -> Error:
        """Delete an inventory item and its offers."""
        return self._call(
            _delete_inventory_item,
            sku=sku,
        )

    @checked
    def get(
        self,
        sku: StrictStr,
    ) -> InventoryItemWithSkuLocaleGroupid:
        """Get one inventory item by SKU."""
        return self._call(
            _get_inventory_item,
            sku=sku,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> InventoryItems:
        """List one page of the seller's inventory items."""
        return self._call(
            _get_inventory_items,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.InventoryItemWithSkuLocaleGroupid]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_inventory_items,
            limit=limit,
            offset=offset,
        )


class AsyncInventoryItemsApi(AsyncResource):
    @checked
    async def bulk_create_or_replace(
        self,
        body: Union[BulkInventoryItem, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BulkInventoryItemResponse:
        """Create or replace several inventory items."""
        return await self._call(
            _bulk_create_or_replace_inventory_item,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def bulk_get(
        self,
        body: Union[BulkGetInventoryItem, Mapping[str, Any]],
    ) -> BulkGetInventoryItemResponse:
        """Get several inventory items by SKU."""
        return await self._call(
            _bulk_get_inventory_item,
            _body=body,
        )

    @checked
    async def bulk_update_price_quantity(
        self,
        body: Union[BulkPriceQuantity, Mapping[str, Any]],
    ) -> BulkPriceQuantityResponse:
        """Update the price and quantity of several inventory items and their offers."""
        return await self._call(
            _bulk_update_price_quantity,
            _body=body,
        )

    @checked
    async def create_or_replace(
        self,
        sku: StrictStr,
        body: Union[InventoryItem, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BaseResponse:
        """Create or replace an inventory item."""
        return await self._call(
            _create_or_replace_inventory_item,
            sku=sku,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def delete(
        self,
        sku: StrictStr,
    ) -> Error:
        """Delete an inventory item and its offers."""
        return await self._call(
            _delete_inventory_item,
            sku=sku,
        )

    @checked
    async def get(
        self,
        sku: StrictStr,
    ) -> InventoryItemWithSkuLocaleGroupid:
        """Get one inventory item by SKU."""
        return await self._call(
            _get_inventory_item,
            sku=sku,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> InventoryItems:
        """List one page of the seller's inventory items."""
        return await self._call(
            _get_inventory_items,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.InventoryItemWithSkuLocaleGroupid]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_inventory_items,
            limit=limit,
            offset=offset,
        )
