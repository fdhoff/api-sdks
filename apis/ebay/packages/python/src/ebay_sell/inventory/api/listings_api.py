# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.inventory.models.bulk_migrate_listing import BulkMigrateListing
from ebay_sell.inventory.models.bulk_migrate_listing_response import BulkMigrateListingResponse
from ebay_sell.inventory.models.location_mapping import LocationMapping

_bulk_migrate_listing: Operation[BulkMigrateListingResponse] = Operation(
    id="bulkMigrateListing",
    method="POST",
    path="/sell/inventory/v1/bulk_migrate_listing",
    resource="listings",
    name="bulk_migrate",
    params=(),
    response=BulkMigrateListingResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_create_or_replace_sku_location_mapping: Operation[None] = Operation(
    id="createOrReplaceSkuLocationMapping",
    method="PUT",
    path="/sell/inventory/v1/listing/{listingId}/sku/{sku}/locations",
    resource="listings",
    name="set_sku_locations",
    params=(
        Param("listingId", "listing_id", "path"),
        Param("sku", "sku", "path"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_delete_sku_location_mapping: Operation[None] = Operation(
    id="deleteSkuLocationMapping",
    method="DELETE",
    path="/sell/inventory/v1/listing/{listingId}/sku/{sku}/locations",
    resource="listings",
    name="delete_sku_locations",
    params=(
        Param("listingId", "listing_id", "path"),
        Param("sku", "sku", "path"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_sku_location_mapping: Operation[LocationMapping] = Operation(
    id="getSkuLocationMapping",
    method="GET",
    path="/sell/inventory/v1/listing/{listingId}/sku/{sku}/locations",
    resource="listings",
    name="get_sku_locations",
    params=(
        Param("listingId", "listing_id", "path"),
        Param("sku", "sku", "path"),
    ),
    response=LocationMapping,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _bulk_migrate_listing,
    _create_or_replace_sku_location_mapping,
    _delete_sku_location_mapping,
    _get_sku_location_mapping,
)


class ListingsApi(Resource):
    @checked
    def bulk_migrate(
        self,
        body: Union[BulkMigrateListing, Mapping[str, Any]],
    ) -> BulkMigrateListingResponse:
        """Move existing listings into the Inventory API."""
        return self._call(
            _bulk_migrate_listing,
            _body=body,
        )

    @checked
    def set_sku_locations(
        self,
        listing_id: StrictStr,
        sku: StrictStr,
        body: Union[LocationMapping, Mapping[str, Any]],
    ) -> None:
        """Set the fulfillment locations of a SKU in a listing."""
        return self._call(
            _create_or_replace_sku_location_mapping,
            listing_id=listing_id,
            sku=sku,
            _body=body,
        )

    @checked
    def delete_sku_locations(
        self,
        listing_id: StrictStr,
        sku: StrictStr,
    ) -> None:
        """Remove the fulfillment locations of a SKU in a listing."""
        return self._call(
            _delete_sku_location_mapping,
            listing_id=listing_id,
            sku=sku,
        )

    @checked
    def get_sku_locations(
        self,
        listing_id: StrictStr,
        sku: StrictStr,
    ) -> LocationMapping:
        """Get the fulfillment locations of a SKU in a listing."""
        return self._call(
            _get_sku_location_mapping,
            listing_id=listing_id,
            sku=sku,
        )


class AsyncListingsApi(AsyncResource):
    @checked
    async def bulk_migrate(
        self,
        body: Union[BulkMigrateListing, Mapping[str, Any]],
    ) -> BulkMigrateListingResponse:
        """Move existing listings into the Inventory API."""
        return await self._call(
            _bulk_migrate_listing,
            _body=body,
        )

    @checked
    async def set_sku_locations(
        self,
        listing_id: StrictStr,
        sku: StrictStr,
        body: Union[LocationMapping, Mapping[str, Any]],
    ) -> None:
        """Set the fulfillment locations of a SKU in a listing."""
        return await self._call(
            _create_or_replace_sku_location_mapping,
            listing_id=listing_id,
            sku=sku,
            _body=body,
        )

    @checked
    async def delete_sku_locations(
        self,
        listing_id: StrictStr,
        sku: StrictStr,
    ) -> None:
        """Remove the fulfillment locations of a SKU in a listing."""
        return await self._call(
            _delete_sku_location_mapping,
            listing_id=listing_id,
            sku=sku,
        )

    @checked
    async def get_sku_locations(
        self,
        listing_id: StrictStr,
        sku: StrictStr,
    ) -> LocationMapping:
        """Get the fulfillment locations of a SKU in a listing."""
        return await self._call(
            _get_sku_location_mapping,
            listing_id=listing_id,
            sku=sku,
        )
