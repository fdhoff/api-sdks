# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.inventory.models.base_response import BaseResponse
from ebay_sell.inventory.models.inventory_item_group import InventoryItemGroup

_create_or_replace_inventory_item_group: Operation[BaseResponse] = Operation(
    id="createOrReplaceInventoryItemGroup",
    method="PUT",
    path="/sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}",
    resource="inventory_item_groups",
    name="create_or_replace",
    params=(
        Param("inventoryItemGroupKey", "inventory_item_group_key", "path"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=BaseResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_delete_inventory_item_group: Operation[None] = Operation(
    id="deleteInventoryItemGroup",
    method="DELETE",
    path="/sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}",
    resource="inventory_item_groups",
    name="delete",
    params=(Param("inventoryItemGroupKey", "inventory_item_group_key", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_inventory_item_group: Operation[InventoryItemGroup] = Operation(
    id="getInventoryItemGroup",
    method="GET",
    path="/sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}",
    resource="inventory_item_groups",
    name="get",
    params=(Param("inventoryItemGroupKey", "inventory_item_group_key", "path"),),
    response=InventoryItemGroup,
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

OPERATIONS = (
    _create_or_replace_inventory_item_group,
    _delete_inventory_item_group,
    _get_inventory_item_group,
)


class InventoryItemGroupsApi(Resource):
    @checked
    def create_or_replace(
        self,
        inventory_item_group_key: StrictStr,
        body: Union[InventoryItemGroup, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BaseResponse:
        """Create or replace an inventory item group for a multi-variation listing."""
        return self._call(
            _create_or_replace_inventory_item_group,
            inventory_item_group_key=inventory_item_group_key,
            _body=body,
            content_language=content_language,
        )

    @checked
    def delete(
        self,
        inventory_item_group_key: StrictStr,
    ) -> None:
        """Delete an inventory item group."""
        return self._call(
            _delete_inventory_item_group,
            inventory_item_group_key=inventory_item_group_key,
        )

    @checked
    def get(
        self,
        inventory_item_group_key: StrictStr,
    ) -> InventoryItemGroup:
        """Get one inventory item group."""
        return self._call(
            _get_inventory_item_group,
            inventory_item_group_key=inventory_item_group_key,
        )


class AsyncInventoryItemGroupsApi(AsyncResource):
    @checked
    async def create_or_replace(
        self,
        inventory_item_group_key: StrictStr,
        body: Union[InventoryItemGroup, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BaseResponse:
        """Create or replace an inventory item group for a multi-variation listing."""
        return await self._call(
            _create_or_replace_inventory_item_group,
            inventory_item_group_key=inventory_item_group_key,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def delete(
        self,
        inventory_item_group_key: StrictStr,
    ) -> None:
        """Delete an inventory item group."""
        return await self._call(
            _delete_inventory_item_group,
            inventory_item_group_key=inventory_item_group_key,
        )

    @checked
    async def get(
        self,
        inventory_item_group_key: StrictStr,
    ) -> InventoryItemGroup:
        """Get one inventory item group."""
        return await self._call(
            _get_inventory_item_group,
            inventory_item_group_key=inventory_item_group_key,
        )
