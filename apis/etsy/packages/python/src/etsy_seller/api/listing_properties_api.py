# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_property_value import ListingPropertyValue
from etsy_seller.models.listing_property_values import ListingPropertyValues

_delete_listing_property: Operation[None] = Operation(
    id="deleteListingProperty",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}",
    resource="listing_properties",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("property_id", "property_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_listing_properties: Operation[ListingPropertyValues] = Operation(
    id="getListingProperties",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/properties",
    resource="listing_properties",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
    ),
    response=ListingPropertyValues,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_listing_property: Operation[ListingPropertyValue] = Operation(
    id="getListingProperty",
    method="GET",
    path="/v3/application/listings/{listing_id}/properties/{property_id}",
    resource="listing_properties",
    name="get",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("property_id", "property_id", "path"),
    ),
    response=ListingPropertyValue,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_listing_property: Operation[ListingPropertyValue] = Operation(
    id="updateListingProperty",
    method="PUT",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}",
    resource="listing_properties",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("property_id", "property_id", "path"),
        Param("value_ids", "value_ids", "urlencoded"),
        Param("values", "values", "urlencoded"),
        Param("scale_id", "scale_id", "urlencoded"),
    ),
    response=ListingPropertyValue,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _delete_listing_property,
    _get_listing_properties,
    _get_listing_property,
    _update_listing_property,
)


class ListingPropertiesApi(Resource):
    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        property_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Remove one property value from a listing."""
        return self._call(
            _delete_listing_property,
            shop_id=shop_id,
            listing_id=listing_id,
            property_id=property_id,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingPropertyValues:
        """List a listing's property values."""
        return self._call(
            _get_listing_properties,
            shop_id=shop_id,
            listing_id=listing_id,
        )

    @checked
    def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        property_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingPropertyValue:
        """Get one property value of a listing."""
        return self._call(
            _get_listing_property,
            listing_id=listing_id,
            property_id=property_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        property_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        value_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        values: List[StrictStr],
        scale_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
    ) -> ListingPropertyValue:
        """Set one property value of a listing."""
        return self._call(
            _update_listing_property,
            shop_id=shop_id,
            listing_id=listing_id,
            property_id=property_id,
            value_ids=value_ids,
            values=values,
            scale_id=scale_id,
        )


class AsyncListingPropertiesApi(AsyncResource):
    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        property_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Remove one property value from a listing."""
        return await self._call(
            _delete_listing_property,
            shop_id=shop_id,
            listing_id=listing_id,
            property_id=property_id,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingPropertyValues:
        """List a listing's property values."""
        return await self._call(
            _get_listing_properties,
            shop_id=shop_id,
            listing_id=listing_id,
        )

    @checked
    async def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        property_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingPropertyValue:
        """Get one property value of a listing."""
        return await self._call(
            _get_listing_property,
            listing_id=listing_id,
            property_id=property_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        property_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        value_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        values: List[StrictStr],
        scale_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
    ) -> ListingPropertyValue:
        """Set one property value of a listing."""
        return await self._call(
            _update_listing_property,
            shop_id=shop_id,
            listing_id=listing_id,
            property_id=property_id,
            value_ids=value_ids,
            values=values,
            scale_id=scale_id,
        )
