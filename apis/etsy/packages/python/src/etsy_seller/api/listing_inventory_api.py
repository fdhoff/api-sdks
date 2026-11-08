# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, List, Mapping, Optional, Union

from pydantic import Field, StrictBool, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_inventory import ListingInventory
from etsy_seller.models.listing_inventory_product import ListingInventoryProduct
from etsy_seller.models.listing_inventory_with_associations import ListingInventoryWithAssociations
from etsy_seller.models.shop_listings_with_associations import ShopListingsWithAssociations
from etsy_seller.models.update_listing_inventory_request import UpdateListingInventoryRequest

_get_listing_inventory: Operation[ListingInventoryWithAssociations] = Operation(
    id="getListingInventory",
    method="GET",
    path="/v3/application/listings/{listing_id}/inventory",
    resource="listing_inventory",
    name="get",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("show_deleted", "show_deleted", "query"),
        Param("includes", "includes", "query"),
    ),
    response=ListingInventoryWithAssociations,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_get_listing_product: Operation[ListingInventoryProduct] = Operation(
    id="getListingProduct",
    method="GET",
    path="/v3/application/listings/{listing_id}/inventory/products/{product_id}",
    resource="listing_inventory",
    name="get_product",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("product_id", "product_id", "path"),
        Param("legacy", "legacy", "query"),
    ),
    response=ListingInventoryProduct,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_get_listings_inventory_by_listing_ids: Operation[ShopListingsWithAssociations] = Operation(
    id="getListingsInventoryByListingIds",
    method="GET",
    path="/v3/application/listings/batch/inventory",
    resource="listing_inventory",
    name="list_by_ids",
    params=(Param("listing_ids", "listing_ids", "query"),),
    response=ShopListingsWithAssociations,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_update_listing_inventory: Operation[ListingInventory] = Operation(
    id="updateListingInventory",
    method="PUT",
    path="/v3/application/listings/{listing_id}/inventory",
    resource="listing_inventory",
    name="update",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("max_variations_supported", "max_variations_supported", "query"),
        Param("enable_scale_validation", "enable_scale_validation", "query"),
    ),
    response=ListingInventory,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _get_listing_inventory,
    _get_listing_product,
    _get_listings_inventory_by_listing_ids,
    _update_listing_inventory,
)


class ListingInventoryApi(Resource):
    @checked
    def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        show_deleted: Optional[StrictBool] = None,
        includes: Optional[StrictStr] = None,
    ) -> ListingInventoryWithAssociations:
        """Get a listing's inventory."""
        return self._call(
            _get_listing_inventory,
            listing_id=listing_id,
            show_deleted=show_deleted,
            includes=includes,
        )

    @checked
    def get_product(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        product_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ListingInventoryProduct:
        """Get one product of a listing's inventory."""
        return self._call(
            _get_listing_product,
            listing_id=listing_id,
            product_id=product_id,
            legacy=legacy,
        )

    @checked
    def list_by_ids(
        self,
        *,
        listing_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> ShopListingsWithAssociations:
        """Get the inventory of several listings by ID."""
        return self._call(
            _get_listings_inventory_by_listing_ids,
            listing_ids=listing_ids,
        )

    @checked
    def update(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[UpdateListingInventoryRequest, Mapping[str, Any]]] = None,
        *,
        max_variations_supported: Optional[StrictStr] = None,
        enable_scale_validation: Optional[StrictBool] = None,
    ) -> ListingInventory:
        """Replace a listing's inventory."""
        return self._call(
            _update_listing_inventory,
            listing_id=listing_id,
            _body=body,
            max_variations_supported=max_variations_supported,
            enable_scale_validation=enable_scale_validation,
        )


class AsyncListingInventoryApi(AsyncResource):
    @checked
    async def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        show_deleted: Optional[StrictBool] = None,
        includes: Optional[StrictStr] = None,
    ) -> ListingInventoryWithAssociations:
        """Get a listing's inventory."""
        return await self._call(
            _get_listing_inventory,
            listing_id=listing_id,
            show_deleted=show_deleted,
            includes=includes,
        )

    @checked
    async def get_product(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        product_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ListingInventoryProduct:
        """Get one product of a listing's inventory."""
        return await self._call(
            _get_listing_product,
            listing_id=listing_id,
            product_id=product_id,
            legacy=legacy,
        )

    @checked
    async def list_by_ids(
        self,
        *,
        listing_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> ShopListingsWithAssociations:
        """Get the inventory of several listings by ID."""
        return await self._call(
            _get_listings_inventory_by_listing_ids,
            listing_ids=listing_ids,
        )

    @checked
    async def update(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[UpdateListingInventoryRequest, Mapping[str, Any]]] = None,
        *,
        max_variations_supported: Optional[StrictStr] = None,
        enable_scale_validation: Optional[StrictBool] = None,
    ) -> ListingInventory:
        """Replace a listing's inventory."""
        return await self._call(
            _update_listing_inventory,
            listing_id=listing_id,
            _body=body,
            max_variations_supported=max_variations_supported,
            enable_scale_validation=enable_scale_validation,
        )
