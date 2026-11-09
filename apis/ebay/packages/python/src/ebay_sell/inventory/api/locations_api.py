# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.inventory import models as _models
from ebay_sell.inventory.models.inventory_location import InventoryLocation
from ebay_sell.inventory.models.inventory_location_full import InventoryLocationFull
from ebay_sell.inventory.models.inventory_location_response import InventoryLocationResponse
from ebay_sell.inventory.models.location_response import LocationResponse

_create_inventory_location: Operation[None] = Operation(
    id="createInventoryLocation",
    method="POST",
    path="/sell/inventory/v1/location/{merchantLocationKey}",
    resource="locations",
    name="create",
    params=(Param("merchantLocationKey", "merchant_location_key", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_delete_inventory_location: Operation[None] = Operation(
    id="deleteInventoryLocation",
    method="DELETE",
    path="/sell/inventory/v1/location/{merchantLocationKey}",
    resource="locations",
    name="delete",
    params=(Param("merchantLocationKey", "merchant_location_key", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_disable_inventory_location: Operation[object] = Operation(
    id="disableInventoryLocation",
    method="POST",
    path="/sell/inventory/v1/location/{merchantLocationKey}/disable",
    resource="locations",
    name="disable",
    params=(Param("merchantLocationKey", "merchant_location_key", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_enable_inventory_location: Operation[object] = Operation(
    id="enableInventoryLocation",
    method="POST",
    path="/sell/inventory/v1/location/{merchantLocationKey}/enable",
    resource="locations",
    name="enable",
    params=(Param("merchantLocationKey", "merchant_location_key", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_inventory_location: Operation[InventoryLocationResponse] = Operation(
    id="getInventoryLocation",
    method="GET",
    path="/sell/inventory/v1/location/{merchantLocationKey}",
    resource="locations",
    name="get",
    params=(Param("merchantLocationKey", "merchant_location_key", "path"),),
    response=InventoryLocationResponse,
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
_get_inventory_locations: Operation[LocationResponse] = Operation(
    id="getInventoryLocations",
    method="GET",
    path="/sell/inventory/v1/location",
    resource="locations",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=LocationResponse,
    returns_json=True,
    iterator="iter",
    item=_models.InventoryLocationResponse,
    paging=NextLink(
        items="locations",
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
_update_inventory_location: Operation[None] = Operation(
    id="updateInventoryLocation",
    method="POST",
    path="/sell/inventory/v1/location/{merchantLocationKey}/update_location_details",
    resource="locations",
    name="update",
    params=(Param("merchantLocationKey", "merchant_location_key", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)

OPERATIONS = (
    _create_inventory_location,
    _delete_inventory_location,
    _disable_inventory_location,
    _enable_inventory_location,
    _get_inventory_location,
    _get_inventory_locations,
    _update_inventory_location,
)


class LocationsApi(Resource):
    @checked
    def create(
        self,
        merchant_location_key: StrictStr,
        body: Union[InventoryLocationFull, Mapping[str, Any]],
    ) -> None:
        """Create an inventory location."""
        return self._call(
            _create_inventory_location,
            merchant_location_key=merchant_location_key,
            _body=body,
        )

    @checked
    def delete(
        self,
        merchant_location_key: StrictStr,
    ) -> None:
        """Delete an inventory location."""
        return self._call(
            _delete_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    def disable(
        self,
        merchant_location_key: StrictStr,
    ) -> object:
        """Disable an inventory location."""
        return self._call(
            _disable_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    def enable(
        self,
        merchant_location_key: StrictStr,
    ) -> object:
        """Enable a disabled inventory location."""
        return self._call(
            _enable_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    def get(
        self,
        merchant_location_key: StrictStr,
    ) -> InventoryLocationResponse:
        """Get one inventory location."""
        return self._call(
            _get_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> LocationResponse:
        """List one page of the seller's inventory locations."""
        return self._call(
            _get_inventory_locations,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.InventoryLocationResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_inventory_locations,
            limit=limit,
            offset=offset,
        )

    @checked
    def update(
        self,
        merchant_location_key: StrictStr,
        body: Union[InventoryLocation, Mapping[str, Any]],
    ) -> None:
        """Update the details of an inventory location."""
        return self._call(
            _update_inventory_location,
            merchant_location_key=merchant_location_key,
            _body=body,
        )


class AsyncLocationsApi(AsyncResource):
    @checked
    async def create(
        self,
        merchant_location_key: StrictStr,
        body: Union[InventoryLocationFull, Mapping[str, Any]],
    ) -> None:
        """Create an inventory location."""
        return await self._call(
            _create_inventory_location,
            merchant_location_key=merchant_location_key,
            _body=body,
        )

    @checked
    async def delete(
        self,
        merchant_location_key: StrictStr,
    ) -> None:
        """Delete an inventory location."""
        return await self._call(
            _delete_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    async def disable(
        self,
        merchant_location_key: StrictStr,
    ) -> object:
        """Disable an inventory location."""
        return await self._call(
            _disable_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    async def enable(
        self,
        merchant_location_key: StrictStr,
    ) -> object:
        """Enable a disabled inventory location."""
        return await self._call(
            _enable_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    async def get(
        self,
        merchant_location_key: StrictStr,
    ) -> InventoryLocationResponse:
        """Get one inventory location."""
        return await self._call(
            _get_inventory_location,
            merchant_location_key=merchant_location_key,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> LocationResponse:
        """List one page of the seller's inventory locations."""
        return await self._call(
            _get_inventory_locations,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.InventoryLocationResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_inventory_locations,
            limit=limit,
            offset=offset,
        )

    @checked
    async def update(
        self,
        merchant_location_key: StrictStr,
        body: Union[InventoryLocation, Mapping[str, Any]],
    ) -> None:
        """Update the details of an inventory location."""
        return await self._call(
            _update_inventory_location,
            merchant_location_key=merchant_location_key,
            _body=body,
        )
