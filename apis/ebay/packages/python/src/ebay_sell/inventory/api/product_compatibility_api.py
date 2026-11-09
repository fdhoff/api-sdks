# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.inventory.models.base_response import BaseResponse
from ebay_sell.inventory.models.compatibility import Compatibility

_create_or_replace_product_compatibility: Operation[BaseResponse] = Operation(
    id="createOrReplaceProductCompatibility",
    method="PUT",
    path="/sell/inventory/v1/inventory_item/{sku}/product_compatibility",
    resource="product_compatibility",
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
_delete_product_compatibility: Operation[None] = Operation(
    id="deleteProductCompatibility",
    method="DELETE",
    path="/sell/inventory/v1/inventory_item/{sku}/product_compatibility",
    resource="product_compatibility",
    name="delete",
    params=(Param("sku", "sku", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_product_compatibility: Operation[Compatibility] = Operation(
    id="getProductCompatibility",
    method="GET",
    path="/sell/inventory/v1/inventory_item/{sku}/product_compatibility",
    resource="product_compatibility",
    name="get",
    params=(Param("sku", "sku", "path"),),
    response=Compatibility,
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
    _create_or_replace_product_compatibility,
    _delete_product_compatibility,
    _get_product_compatibility,
)


class ProductCompatibilityApi(Resource):
    @checked
    def create_or_replace(
        self,
        sku: StrictStr,
        body: Union[Compatibility, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BaseResponse:
        """Set the vehicles an inventory item fits."""
        return self._call(
            _create_or_replace_product_compatibility,
            sku=sku,
            _body=body,
            content_language=content_language,
        )

    @checked
    def delete(
        self,
        sku: StrictStr,
    ) -> None:
        """Remove the vehicle list of an inventory item."""
        return self._call(
            _delete_product_compatibility,
            sku=sku,
        )

    @checked
    def get(
        self,
        sku: StrictStr,
    ) -> Compatibility:
        """Get the vehicles an inventory item fits."""
        return self._call(
            _get_product_compatibility,
            sku=sku,
        )


class AsyncProductCompatibilityApi(AsyncResource):
    @checked
    async def create_or_replace(
        self,
        sku: StrictStr,
        body: Union[Compatibility, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BaseResponse:
        """Set the vehicles an inventory item fits."""
        return await self._call(
            _create_or_replace_product_compatibility,
            sku=sku,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def delete(
        self,
        sku: StrictStr,
    ) -> None:
        """Remove the vehicle list of an inventory item."""
        return await self._call(
            _delete_product_compatibility,
            sku=sku,
        )

    @checked
    async def get(
        self,
        sku: StrictStr,
    ) -> Compatibility:
        """Get the vehicles an inventory item fits."""
        return await self._call(
            _get_product_compatibility,
            sku=sku,
        )
