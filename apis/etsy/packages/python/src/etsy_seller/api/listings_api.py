# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, List, Optional

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_listing import ShopListing
from etsy_seller.models.shop_listing_with_associations import ShopListingWithAssociations
from etsy_seller.models.shop_listings import ShopListings
from etsy_seller.models.shop_listings_with_associations import ShopListingsWithAssociations

_create_draft_listing: Operation[ShopListing] = Operation(
    id="createDraftListing",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings",
    resource="listings",
    name="create_draft",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("quantity", "quantity", "urlencoded"),
        Param("title", "title", "urlencoded"),
        Param("description", "description", "urlencoded"),
        Param("price", "price", "urlencoded"),
        Param("who_made", "who_made", "urlencoded"),
        Param("when_made", "when_made", "urlencoded"),
        Param("taxonomy_id", "taxonomy_id", "urlencoded"),
        Param("shipping_profile_id", "shipping_profile_id", "urlencoded"),
        Param("return_policy_id", "return_policy_id", "urlencoded"),
        Param("materials", "materials", "urlencoded"),
        Param("shop_section_id", "shop_section_id", "urlencoded"),
        Param("processing_min", "processing_min", "urlencoded"),
        Param("processing_max", "processing_max", "urlencoded"),
        Param("readiness_state_id", "readiness_state_id", "urlencoded"),
        Param("tags", "tags", "urlencoded"),
        Param("styles", "styles", "urlencoded"),
        Param("item_weight", "item_weight", "urlencoded"),
        Param("item_length", "item_length", "urlencoded"),
        Param("item_width", "item_width", "urlencoded"),
        Param("item_height", "item_height", "urlencoded"),
        Param("item_weight_unit", "item_weight_unit", "urlencoded"),
        Param("item_dimensions_unit", "item_dimensions_unit", "urlencoded"),
        Param("production_partner_ids", "production_partner_ids", "urlencoded"),
        Param("image_ids", "image_ids", "urlencoded"),
        Param("ecgt_garan_brand", "ecgt_garan_brand", "urlencoded"),
        Param("ecgt_garan_years", "ecgt_garan_years", "urlencoded"),
        Param("ecgt_garan_model", "ecgt_garan_model", "urlencoded"),
        Param("ecgt_garan_guarantee_details", "ecgt_garan_guarantee_details", "urlencoded"),
        Param("ecgt_other_commercial_guarantee_details", "ecgt_other_commercial_guarantee_details", "urlencoded"),
        Param("ecgt_after_sales_service_info", "ecgt_after_sales_service_info", "urlencoded"),
        Param("ecgt_software_update_details", "ecgt_software_update_details", "urlencoded"),
        Param("gpsr_manufacturer_type", "gpsr_manufacturer_type", "urlencoded"),
        Param("gpsr_manufacturer_id", "gpsr_manufacturer_id", "urlencoded"),
        Param("gpsr_responsible_person_type", "gpsr_responsible_person_type", "urlencoded"),
        Param("gpsr_responsible_person_id", "gpsr_responsible_person_id", "urlencoded"),
        Param("gpsr_serial_number", "gpsr_serial_number", "urlencoded"),
        Param("gpsr_safety_warnings", "gpsr_safety_warnings", "urlencoded"),
        Param("is_supply", "is_supply", "urlencoded"),
        Param("is_customizable", "is_customizable", "urlencoded"),
        Param("should_auto_renew", "should_auto_renew", "urlencoded"),
        Param("is_taxable", "is_taxable", "urlencoded"),
        Param("type", "type", "urlencoded"),
    ),
    response=ShopListing,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_delete_listing: Operation[None] = Operation(
    id="deleteListing",
    method="DELETE",
    path="/v3/application/listings/{listing_id}",
    resource="listings",
    name="delete",
    params=(Param("listing_id", "listing_id", "path"),),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_d",)),
        ),
    ),
)
_find_all_active_listings_by_shop: Operation[ShopListings] = Operation(
    id="findAllActiveListingsByShop",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/active",
    resource="listings",
    name="list_active_by_shop",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("limit", "limit", "query"),
        Param("sort_on", "sort_on", "query"),
        Param("sort_order", "sort_order", "query"),
        Param("offset", "offset", "query"),
        Param("keywords", "keywords", "query"),
    ),
    response=ShopListings,
    returns_json=True,
    iterator="iter_active_by_shop",
    item=_models.ShopListing,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)
_find_all_listings_active: Operation[ShopListings] = Operation(
    id="findAllListingsActive",
    method="GET",
    path="/v3/application/listings/active",
    resource="listings",
    name="list_active",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("keywords", "keywords", "query"),
        Param("sort_on", "sort_on", "query"),
        Param("sort_order", "sort_order", "query"),
        Param("min_price", "min_price", "query"),
        Param("max_price", "max_price", "query"),
        Param("taxonomy_id", "taxonomy_id", "query"),
        Param("shop_location", "shop_location", "query"),
        Param("is_safe", "is_safe", "query"),
        Param("currency", "currency", "query"),
        Param("buyer_country", "buyer_country", "query"),
    ),
    response=ShopListings,
    returns_json=True,
    iterator="iter_active",
    item=_models.ShopListing,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)
_get_featured_listings_by_shop: Operation[ShopListings] = Operation(
    id="getFeaturedListingsByShop",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/featured",
    resource="listings",
    name="list_featured",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopListings,
    returns_json=True,
    iterator="iter_featured",
    item=_models.ShopListing,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)
_get_listing: Operation[ShopListingWithAssociations] = Operation(
    id="getListing",
    method="GET",
    path="/v3/application/listings/{listing_id}",
    resource="listings",
    name="get",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("includes", "includes", "query"),
        Param("language", "language", "query"),
        Param("allow_suggested_title", "allow_suggested_title", "query"),
    ),
    response=ShopListingWithAssociations,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_listings_by_listing_ids: Operation[ShopListingsWithAssociations] = Operation(
    id="getListingsByListingIds",
    method="GET",
    path="/v3/application/listings/batch",
    resource="listings",
    name="list_by_ids",
    params=(
        Param("listing_ids", "listing_ids", "query"),
        Param("includes", "includes", "query"),
        Param("legacy", "legacy", "query"),
        Param("currency", "currency", "query"),
        Param("buyer_country", "buyer_country", "query"),
    ),
    response=ShopListingsWithAssociations,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_listings_by_shop: Operation[ShopListingsWithAssociations] = Operation(
    id="getListingsByShop",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings",
    resource="listings",
    name="list_by_shop",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("state", "state", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort_on", "sort_on", "query"),
        Param("sort_order", "sort_order", "query"),
        Param("includes", "includes", "query"),
    ),
    response=ShopListingsWithAssociations,
    returns_json=True,
    iterator="iter_by_shop",
    item=_models.ShopListingWithAssociations,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_get_listings_by_shop_receipt: Operation[ShopListings] = Operation(
    id="getListingsByShopReceipt",
    method="GET",
    path="/v3/application/shops/{shop_id}/receipts/{receipt_id}/listings",
    resource="listings",
    name="list_by_receipt",
    params=(
        Param("receipt_id", "receipt_id", "path"),
        Param("shop_id", "shop_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopListings,
    returns_json=True,
    iterator="iter_by_receipt",
    item=_models.ShopListing,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_listings_by_shop_return_policy: Operation[ShopListings] = Operation(
    id="getListingsByShopReturnPolicy",
    method="GET",
    path="/v3/application/shops/{shop_id}/policies/return/{return_policy_id}/listings",
    resource="listings",
    name="list_by_return_policy",
    params=(
        Param("return_policy_id", "return_policy_id", "path"),
        Param("shop_id", "shop_id", "path"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopListings,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_get_listings_by_shop_section_id: Operation[ShopListings] = Operation(
    id="getListingsByShopSectionId",
    method="GET",
    path="/v3/application/shops/{shop_id}/shop-sections/listings",
    resource="listings",
    name="list_by_sections",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shop_section_ids", "shop_section_ids", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort_on", "sort_on", "query"),
        Param("sort_order", "sort_order", "query"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopListings,
    returns_json=True,
    iterator="iter_by_sections",
    item=_models.ShopListing,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)
_get_listings_shipping_by_listing_ids: Operation[ShopListingsWithAssociations] = Operation(
    id="getListingsShippingByListingIds",
    method="GET",
    path="/v3/application/listings/batch/shipping",
    resource="listings",
    name="list_shipping_by_ids",
    params=(Param("listing_ids", "listing_ids", "query"),),
    response=ShopListingsWithAssociations,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_update_listing: Operation[ShopListing] = Operation(
    id="updateListing",
    method="PATCH",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}",
    resource="listings",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("image_ids", "image_ids", "urlencoded"),
        Param("title", "title", "urlencoded"),
        Param("description", "description", "urlencoded"),
        Param("materials", "materials", "urlencoded"),
        Param("should_auto_renew", "should_auto_renew", "urlencoded"),
        Param("shipping_profile_id", "shipping_profile_id", "urlencoded"),
        Param("return_policy_id", "return_policy_id", "urlencoded"),
        Param("shop_section_id", "shop_section_id", "urlencoded"),
        Param("item_weight", "item_weight", "urlencoded"),
        Param("item_length", "item_length", "urlencoded"),
        Param("item_width", "item_width", "urlencoded"),
        Param("item_height", "item_height", "urlencoded"),
        Param("item_weight_unit", "item_weight_unit", "urlencoded"),
        Param("item_dimensions_unit", "item_dimensions_unit", "urlencoded"),
        Param("is_taxable", "is_taxable", "urlencoded"),
        Param("taxonomy_id", "taxonomy_id", "urlencoded"),
        Param("tags", "tags", "urlencoded"),
        Param("who_made", "who_made", "urlencoded"),
        Param("when_made", "when_made", "urlencoded"),
        Param("state", "state", "urlencoded"),
        Param("is_supply", "is_supply", "urlencoded"),
        Param("production_partner_ids", "production_partner_ids", "urlencoded"),
        Param("type", "type", "urlencoded"),
        Param("ecgt_garan_brand", "ecgt_garan_brand", "urlencoded"),
        Param("ecgt_garan_years", "ecgt_garan_years", "urlencoded"),
        Param("ecgt_garan_model", "ecgt_garan_model", "urlencoded"),
        Param("ecgt_garan_guarantee_details", "ecgt_garan_guarantee_details", "urlencoded"),
        Param("ecgt_other_commercial_guarantee_details", "ecgt_other_commercial_guarantee_details", "urlencoded"),
        Param("ecgt_after_sales_service_info", "ecgt_after_sales_service_info", "urlencoded"),
        Param("ecgt_software_update_details", "ecgt_software_update_details", "urlencoded"),
        Param("gpsr_manufacturer_type", "gpsr_manufacturer_type", "urlencoded"),
        Param("gpsr_manufacturer_id", "gpsr_manufacturer_id", "urlencoded"),
        Param("gpsr_responsible_person_type", "gpsr_responsible_person_type", "urlencoded"),
        Param("gpsr_responsible_person_id", "gpsr_responsible_person_id", "urlencoded"),
        Param("gpsr_serial_number", "gpsr_serial_number", "urlencoded"),
        Param("gpsr_safety_warnings", "gpsr_safety_warnings", "urlencoded"),
    ),
    response=ShopListing,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_draft_listing,
    _delete_listing,
    _find_all_active_listings_by_shop,
    _find_all_listings_active,
    _get_featured_listings_by_shop,
    _get_listing,
    _get_listings_by_listing_ids,
    _get_listings_by_shop,
    _get_listings_by_shop_receipt,
    _get_listings_by_shop_return_policy,
    _get_listings_by_shop_section_id,
    _get_listings_shipping_by_listing_ids,
    _update_listing,
)


class ListingsApi(Resource):
    @checked
    def create_draft(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        quantity: StrictInt,
        title: StrictStr,
        description: StrictStr,
        price: float,
        who_made: StrictStr,
        when_made: StrictStr,
        taxonomy_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        materials: Optional[List[StrictStr]] = None,
        shop_section_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        processing_min: Optional[StrictInt] = None,
        processing_max: Optional[StrictInt] = None,
        readiness_state_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        tags: Optional[List[StrictStr]] = None,
        styles: Optional[List[StrictStr]] = None,
        item_weight: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_length: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_width: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_height: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_weight_unit: Optional[StrictStr] = None,
        item_dimensions_unit: Optional[StrictStr] = None,
        production_partner_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        image_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        ecgt_garan_brand: Optional[StrictStr] = None,
        ecgt_garan_years: Optional[StrictInt] = None,
        ecgt_garan_model: Optional[StrictStr] = None,
        ecgt_garan_guarantee_details: Optional[StrictStr] = None,
        ecgt_other_commercial_guarantee_details: Optional[StrictStr] = None,
        ecgt_after_sales_service_info: Optional[StrictStr] = None,
        ecgt_software_update_details: Optional[StrictStr] = None,
        gpsr_manufacturer_type: Optional[StrictStr] = None,
        gpsr_manufacturer_id: Optional[StrictInt] = None,
        gpsr_responsible_person_type: Optional[StrictStr] = None,
        gpsr_responsible_person_id: Optional[StrictInt] = None,
        gpsr_serial_number: Optional[StrictStr] = None,
        gpsr_safety_warnings: Optional[StrictStr] = None,
        is_supply: Optional[StrictBool] = None,
        is_customizable: Optional[StrictBool] = None,
        should_auto_renew: Optional[StrictBool] = None,
        is_taxable: Optional[StrictBool] = None,
        type: Optional[StrictStr] = None,
    ) -> ShopListing:
        """Create a draft listing."""
        return self._call(
            _create_draft_listing,
            shop_id=shop_id,
            quantity=quantity,
            title=title,
            description=description,
            price=price,
            who_made=who_made,
            when_made=when_made,
            taxonomy_id=taxonomy_id,
            shipping_profile_id=shipping_profile_id,
            return_policy_id=return_policy_id,
            materials=materials,
            shop_section_id=shop_section_id,
            processing_min=processing_min,
            processing_max=processing_max,
            readiness_state_id=readiness_state_id,
            tags=tags,
            styles=styles,
            item_weight=item_weight,
            item_length=item_length,
            item_width=item_width,
            item_height=item_height,
            item_weight_unit=item_weight_unit,
            item_dimensions_unit=item_dimensions_unit,
            production_partner_ids=production_partner_ids,
            image_ids=image_ids,
            ecgt_garan_brand=ecgt_garan_brand,
            ecgt_garan_years=ecgt_garan_years,
            ecgt_garan_model=ecgt_garan_model,
            ecgt_garan_guarantee_details=ecgt_garan_guarantee_details,
            ecgt_other_commercial_guarantee_details=ecgt_other_commercial_guarantee_details,
            ecgt_after_sales_service_info=ecgt_after_sales_service_info,
            ecgt_software_update_details=ecgt_software_update_details,
            gpsr_manufacturer_type=gpsr_manufacturer_type,
            gpsr_manufacturer_id=gpsr_manufacturer_id,
            gpsr_responsible_person_type=gpsr_responsible_person_type,
            gpsr_responsible_person_id=gpsr_responsible_person_id,
            gpsr_serial_number=gpsr_serial_number,
            gpsr_safety_warnings=gpsr_safety_warnings,
            is_supply=is_supply,
            is_customizable=is_customizable,
            should_auto_renew=should_auto_renew,
            is_taxable=is_taxable,
            type=type,
        )

    @checked
    def delete(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a listing."""
        return self._call(
            _delete_listing,
            listing_id=listing_id,
        )

    @checked
    def list_active_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
    ) -> ShopListings:
        """List one page of a shop's active listings."""
        return self._call(
            _find_all_active_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            sort_on=sort_on,
            sort_order=sort_order,
            offset=offset,
            keywords=keywords,
        )

    @checked
    def iter_active_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
    ) -> Iterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_all_active_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            sort_on=sort_on,
            sort_order=sort_order,
            offset=offset,
            keywords=keywords,
        )

    @checked
    def list_active(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        taxonomy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        shop_location: Optional[StrictStr] = None,
        is_safe: Optional[StrictBool] = None,
        currency: Optional[StrictStr] = None,
        buyer_country: Optional[StrictStr] = None,
    ) -> ShopListings:
        """Search one page of active listings across all shops."""
        return self._call(
            _find_all_listings_active,
            limit=limit,
            offset=offset,
            keywords=keywords,
            sort_on=sort_on,
            sort_order=sort_order,
            min_price=min_price,
            max_price=max_price,
            taxonomy_id=taxonomy_id,
            shop_location=shop_location,
            is_safe=is_safe,
            currency=currency,
            buyer_country=buyer_country,
        )

    @checked
    def iter_active(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        taxonomy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        shop_location: Optional[StrictStr] = None,
        is_safe: Optional[StrictBool] = None,
        currency: Optional[StrictStr] = None,
        buyer_country: Optional[StrictStr] = None,
    ) -> Iterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_all_listings_active,
            limit=limit,
            offset=offset,
            keywords=keywords,
            sort_on=sort_on,
            sort_order=sort_order,
            min_price=min_price,
            max_price=max_price,
            taxonomy_id=taxonomy_id,
            shop_location=shop_location,
            is_safe=is_safe,
            currency=currency,
            buyer_country=buyer_country,
        )

    @checked
    def list_featured(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List one page of a shop's featured listings."""
        return self._call(
            _get_featured_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter_featured(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> Iterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_featured_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        includes: Optional[List[StrictStr]] = None,
        language: Optional[StrictStr] = None,
        allow_suggested_title: Optional[StrictBool] = None,
    ) -> ShopListingWithAssociations:
        """Get one listing."""
        return self._call(
            _get_listing,
            listing_id=listing_id,
            includes=includes,
            language=language,
            allow_suggested_title=allow_suggested_title,
        )

    @checked
    def list_by_ids(
        self,
        *,
        listing_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        includes: Optional[List[StrictStr]] = None,
        legacy: Optional[StrictBool] = None,
        currency: Optional[StrictStr] = None,
        buyer_country: Optional[StrictStr] = None,
    ) -> ShopListingsWithAssociations:
        """Get several listings by ID."""
        return self._call(
            _get_listings_by_listing_ids,
            listing_ids=listing_ids,
            includes=includes,
            legacy=legacy,
            currency=currency,
            buyer_country=buyer_country,
        )

    @checked
    def list_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        state: Optional[StrictStr] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        includes: Optional[List[StrictStr]] = None,
    ) -> ShopListingsWithAssociations:
        """List one page of a shop's listings in any state."""
        return self._call(
            _get_listings_by_shop,
            shop_id=shop_id,
            state=state,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            includes=includes,
        )

    @checked
    def iter_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        state: Optional[StrictStr] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        includes: Optional[List[StrictStr]] = None,
    ) -> Iterator[_models.ShopListingWithAssociations]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listings_by_shop,
            shop_id=shop_id,
            state=state,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            includes=includes,
        )

    @checked
    def list_by_receipt(
        self,
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List one page of the listings on a receipt."""
        return self._call(
            _get_listings_by_shop_receipt,
            receipt_id=receipt_id,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter_by_receipt(
        self,
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> Iterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listings_by_shop_receipt,
            receipt_id=receipt_id,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def list_by_return_policy(
        self,
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List the listings that use a return policy."""
        return self._call(
            _get_listings_by_shop_return_policy,
            return_policy_id=return_policy_id,
            shop_id=shop_id,
            legacy=legacy,
        )

    @checked
    def list_by_sections(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        shop_section_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List one page of the listings in shop sections."""
        return self._call(
            _get_listings_by_shop_section_id,
            shop_id=shop_id,
            shop_section_ids=shop_section_ids,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            legacy=legacy,
        )

    @checked
    def iter_by_sections(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        shop_section_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        legacy: Optional[StrictBool] = None,
    ) -> Iterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listings_by_shop_section_id,
            shop_id=shop_id,
            shop_section_ids=shop_section_ids,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            legacy=legacy,
        )

    @checked
    def list_shipping_by_ids(
        self,
        *,
        listing_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> ShopListingsWithAssociations:
        """Get the shipping details of several listings by ID."""
        return self._call(
            _get_listings_shipping_by_listing_ids,
            listing_ids=listing_ids,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        image_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        title: Optional[StrictStr] = None,
        description: Optional[StrictStr] = None,
        materials: Optional[List[StrictStr]] = None,
        should_auto_renew: Optional[StrictBool] = None,
        shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        shop_section_id: Optional[StrictInt] = None,
        item_weight: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_length: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_width: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_height: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_weight_unit: Optional[StrictStr] = None,
        item_dimensions_unit: Optional[StrictStr] = None,
        is_taxable: Optional[StrictBool] = None,
        taxonomy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        tags: Optional[List[StrictStr]] = None,
        who_made: Optional[StrictStr] = None,
        when_made: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        is_supply: Optional[StrictBool] = None,
        production_partner_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        type: Optional[StrictStr] = None,
        ecgt_garan_brand: Optional[StrictStr] = None,
        ecgt_garan_years: Optional[StrictInt] = None,
        ecgt_garan_model: Optional[StrictStr] = None,
        ecgt_garan_guarantee_details: Optional[StrictStr] = None,
        ecgt_other_commercial_guarantee_details: Optional[StrictStr] = None,
        ecgt_after_sales_service_info: Optional[StrictStr] = None,
        ecgt_software_update_details: Optional[StrictStr] = None,
        gpsr_manufacturer_type: Optional[StrictStr] = None,
        gpsr_manufacturer_id: Optional[StrictInt] = None,
        gpsr_responsible_person_type: Optional[StrictStr] = None,
        gpsr_responsible_person_id: Optional[StrictInt] = None,
        gpsr_serial_number: Optional[StrictStr] = None,
        gpsr_safety_warnings: Optional[StrictStr] = None,
    ) -> ShopListing:
        """Update a listing."""
        return self._call(
            _update_listing,
            shop_id=shop_id,
            listing_id=listing_id,
            image_ids=image_ids,
            title=title,
            description=description,
            materials=materials,
            should_auto_renew=should_auto_renew,
            shipping_profile_id=shipping_profile_id,
            return_policy_id=return_policy_id,
            shop_section_id=shop_section_id,
            item_weight=item_weight,
            item_length=item_length,
            item_width=item_width,
            item_height=item_height,
            item_weight_unit=item_weight_unit,
            item_dimensions_unit=item_dimensions_unit,
            is_taxable=is_taxable,
            taxonomy_id=taxonomy_id,
            tags=tags,
            who_made=who_made,
            when_made=when_made,
            state=state,
            is_supply=is_supply,
            production_partner_ids=production_partner_ids,
            type=type,
            ecgt_garan_brand=ecgt_garan_brand,
            ecgt_garan_years=ecgt_garan_years,
            ecgt_garan_model=ecgt_garan_model,
            ecgt_garan_guarantee_details=ecgt_garan_guarantee_details,
            ecgt_other_commercial_guarantee_details=ecgt_other_commercial_guarantee_details,
            ecgt_after_sales_service_info=ecgt_after_sales_service_info,
            ecgt_software_update_details=ecgt_software_update_details,
            gpsr_manufacturer_type=gpsr_manufacturer_type,
            gpsr_manufacturer_id=gpsr_manufacturer_id,
            gpsr_responsible_person_type=gpsr_responsible_person_type,
            gpsr_responsible_person_id=gpsr_responsible_person_id,
            gpsr_serial_number=gpsr_serial_number,
            gpsr_safety_warnings=gpsr_safety_warnings,
        )


class AsyncListingsApi(AsyncResource):
    @checked
    async def create_draft(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        quantity: StrictInt,
        title: StrictStr,
        description: StrictStr,
        price: float,
        who_made: StrictStr,
        when_made: StrictStr,
        taxonomy_id: Annotated[int, Field(strict=True, ge=1)],
        shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        materials: Optional[List[StrictStr]] = None,
        shop_section_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        processing_min: Optional[StrictInt] = None,
        processing_max: Optional[StrictInt] = None,
        readiness_state_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        tags: Optional[List[StrictStr]] = None,
        styles: Optional[List[StrictStr]] = None,
        item_weight: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_length: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_width: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_height: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_weight_unit: Optional[StrictStr] = None,
        item_dimensions_unit: Optional[StrictStr] = None,
        production_partner_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        image_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        ecgt_garan_brand: Optional[StrictStr] = None,
        ecgt_garan_years: Optional[StrictInt] = None,
        ecgt_garan_model: Optional[StrictStr] = None,
        ecgt_garan_guarantee_details: Optional[StrictStr] = None,
        ecgt_other_commercial_guarantee_details: Optional[StrictStr] = None,
        ecgt_after_sales_service_info: Optional[StrictStr] = None,
        ecgt_software_update_details: Optional[StrictStr] = None,
        gpsr_manufacturer_type: Optional[StrictStr] = None,
        gpsr_manufacturer_id: Optional[StrictInt] = None,
        gpsr_responsible_person_type: Optional[StrictStr] = None,
        gpsr_responsible_person_id: Optional[StrictInt] = None,
        gpsr_serial_number: Optional[StrictStr] = None,
        gpsr_safety_warnings: Optional[StrictStr] = None,
        is_supply: Optional[StrictBool] = None,
        is_customizable: Optional[StrictBool] = None,
        should_auto_renew: Optional[StrictBool] = None,
        is_taxable: Optional[StrictBool] = None,
        type: Optional[StrictStr] = None,
    ) -> ShopListing:
        """Create a draft listing."""
        return await self._call(
            _create_draft_listing,
            shop_id=shop_id,
            quantity=quantity,
            title=title,
            description=description,
            price=price,
            who_made=who_made,
            when_made=when_made,
            taxonomy_id=taxonomy_id,
            shipping_profile_id=shipping_profile_id,
            return_policy_id=return_policy_id,
            materials=materials,
            shop_section_id=shop_section_id,
            processing_min=processing_min,
            processing_max=processing_max,
            readiness_state_id=readiness_state_id,
            tags=tags,
            styles=styles,
            item_weight=item_weight,
            item_length=item_length,
            item_width=item_width,
            item_height=item_height,
            item_weight_unit=item_weight_unit,
            item_dimensions_unit=item_dimensions_unit,
            production_partner_ids=production_partner_ids,
            image_ids=image_ids,
            ecgt_garan_brand=ecgt_garan_brand,
            ecgt_garan_years=ecgt_garan_years,
            ecgt_garan_model=ecgt_garan_model,
            ecgt_garan_guarantee_details=ecgt_garan_guarantee_details,
            ecgt_other_commercial_guarantee_details=ecgt_other_commercial_guarantee_details,
            ecgt_after_sales_service_info=ecgt_after_sales_service_info,
            ecgt_software_update_details=ecgt_software_update_details,
            gpsr_manufacturer_type=gpsr_manufacturer_type,
            gpsr_manufacturer_id=gpsr_manufacturer_id,
            gpsr_responsible_person_type=gpsr_responsible_person_type,
            gpsr_responsible_person_id=gpsr_responsible_person_id,
            gpsr_serial_number=gpsr_serial_number,
            gpsr_safety_warnings=gpsr_safety_warnings,
            is_supply=is_supply,
            is_customizable=is_customizable,
            should_auto_renew=should_auto_renew,
            is_taxable=is_taxable,
            type=type,
        )

    @checked
    async def delete(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a listing."""
        return await self._call(
            _delete_listing,
            listing_id=listing_id,
        )

    @checked
    async def list_active_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
    ) -> ShopListings:
        """List one page of a shop's active listings."""
        return await self._call(
            _find_all_active_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            sort_on=sort_on,
            sort_order=sort_order,
            offset=offset,
            keywords=keywords,
        )

    @checked
    def iter_active_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_all_active_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            sort_on=sort_on,
            sort_order=sort_order,
            offset=offset,
            keywords=keywords,
        )

    @checked
    async def list_active(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        taxonomy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        shop_location: Optional[StrictStr] = None,
        is_safe: Optional[StrictBool] = None,
        currency: Optional[StrictStr] = None,
        buyer_country: Optional[StrictStr] = None,
    ) -> ShopListings:
        """Search one page of active listings across all shops."""
        return await self._call(
            _find_all_listings_active,
            limit=limit,
            offset=offset,
            keywords=keywords,
            sort_on=sort_on,
            sort_order=sort_order,
            min_price=min_price,
            max_price=max_price,
            taxonomy_id=taxonomy_id,
            shop_location=shop_location,
            is_safe=is_safe,
            currency=currency,
            buyer_country=buyer_country,
        )

    @checked
    def iter_active(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        keywords: Optional[StrictStr] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        taxonomy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        shop_location: Optional[StrictStr] = None,
        is_safe: Optional[StrictBool] = None,
        currency: Optional[StrictStr] = None,
        buyer_country: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_all_listings_active,
            limit=limit,
            offset=offset,
            keywords=keywords,
            sort_on=sort_on,
            sort_order=sort_order,
            min_price=min_price,
            max_price=max_price,
            taxonomy_id=taxonomy_id,
            shop_location=shop_location,
            is_safe=is_safe,
            currency=currency,
            buyer_country=buyer_country,
        )

    @checked
    async def list_featured(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List one page of a shop's featured listings."""
        return await self._call(
            _get_featured_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter_featured(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_featured_listings_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    async def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        includes: Optional[List[StrictStr]] = None,
        language: Optional[StrictStr] = None,
        allow_suggested_title: Optional[StrictBool] = None,
    ) -> ShopListingWithAssociations:
        """Get one listing."""
        return await self._call(
            _get_listing,
            listing_id=listing_id,
            includes=includes,
            language=language,
            allow_suggested_title=allow_suggested_title,
        )

    @checked
    async def list_by_ids(
        self,
        *,
        listing_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        includes: Optional[List[StrictStr]] = None,
        legacy: Optional[StrictBool] = None,
        currency: Optional[StrictStr] = None,
        buyer_country: Optional[StrictStr] = None,
    ) -> ShopListingsWithAssociations:
        """Get several listings by ID."""
        return await self._call(
            _get_listings_by_listing_ids,
            listing_ids=listing_ids,
            includes=includes,
            legacy=legacy,
            currency=currency,
            buyer_country=buyer_country,
        )

    @checked
    async def list_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        state: Optional[StrictStr] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        includes: Optional[List[StrictStr]] = None,
    ) -> ShopListingsWithAssociations:
        """List one page of a shop's listings in any state."""
        return await self._call(
            _get_listings_by_shop,
            shop_id=shop_id,
            state=state,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            includes=includes,
        )

    @checked
    def iter_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        state: Optional[StrictStr] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        includes: Optional[List[StrictStr]] = None,
    ) -> AsyncIterator[_models.ShopListingWithAssociations]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listings_by_shop,
            shop_id=shop_id,
            state=state,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            includes=includes,
        )

    @checked
    async def list_by_receipt(
        self,
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List one page of the listings on a receipt."""
        return await self._call(
            _get_listings_by_shop_receipt,
            receipt_id=receipt_id,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter_by_receipt(
        self,
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listings_by_shop_receipt,
            receipt_id=receipt_id,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    async def list_by_return_policy(
        self,
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List the listings that use a return policy."""
        return await self._call(
            _get_listings_by_shop_return_policy,
            return_policy_id=return_policy_id,
            shop_id=shop_id,
            legacy=legacy,
        )

    @checked
    async def list_by_sections(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        shop_section_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopListings:
        """List one page of the listings in shop sections."""
        return await self._call(
            _get_listings_by_shop_section_id,
            shop_id=shop_id,
            shop_section_ids=shop_section_ids,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            legacy=legacy,
        )

    @checked
    def iter_by_sections(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        shop_section_ids: List[Annotated[int, Field(strict=True, ge=1)]],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        legacy: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ShopListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listings_by_shop_section_id,
            shop_id=shop_id,
            shop_section_ids=shop_section_ids,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            legacy=legacy,
        )

    @checked
    async def list_shipping_by_ids(
        self,
        *,
        listing_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> ShopListingsWithAssociations:
        """Get the shipping details of several listings by ID."""
        return await self._call(
            _get_listings_shipping_by_listing_ids,
            listing_ids=listing_ids,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        image_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        title: Optional[StrictStr] = None,
        description: Optional[StrictStr] = None,
        materials: Optional[List[StrictStr]] = None,
        should_auto_renew: Optional[StrictBool] = None,
        shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        shop_section_id: Optional[StrictInt] = None,
        item_weight: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_length: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_width: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_height: Optional[Annotated[float, Field(le=1.79769313486e308, ge=0)]] = None,
        item_weight_unit: Optional[StrictStr] = None,
        item_dimensions_unit: Optional[StrictStr] = None,
        is_taxable: Optional[StrictBool] = None,
        taxonomy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        tags: Optional[List[StrictStr]] = None,
        who_made: Optional[StrictStr] = None,
        when_made: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        is_supply: Optional[StrictBool] = None,
        production_partner_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None,
        type: Optional[StrictStr] = None,
        ecgt_garan_brand: Optional[StrictStr] = None,
        ecgt_garan_years: Optional[StrictInt] = None,
        ecgt_garan_model: Optional[StrictStr] = None,
        ecgt_garan_guarantee_details: Optional[StrictStr] = None,
        ecgt_other_commercial_guarantee_details: Optional[StrictStr] = None,
        ecgt_after_sales_service_info: Optional[StrictStr] = None,
        ecgt_software_update_details: Optional[StrictStr] = None,
        gpsr_manufacturer_type: Optional[StrictStr] = None,
        gpsr_manufacturer_id: Optional[StrictInt] = None,
        gpsr_responsible_person_type: Optional[StrictStr] = None,
        gpsr_responsible_person_id: Optional[StrictInt] = None,
        gpsr_serial_number: Optional[StrictStr] = None,
        gpsr_safety_warnings: Optional[StrictStr] = None,
    ) -> ShopListing:
        """Update a listing."""
        return await self._call(
            _update_listing,
            shop_id=shop_id,
            listing_id=listing_id,
            image_ids=image_ids,
            title=title,
            description=description,
            materials=materials,
            should_auto_renew=should_auto_renew,
            shipping_profile_id=shipping_profile_id,
            return_policy_id=return_policy_id,
            shop_section_id=shop_section_id,
            item_weight=item_weight,
            item_length=item_length,
            item_width=item_width,
            item_height=item_height,
            item_weight_unit=item_weight_unit,
            item_dimensions_unit=item_dimensions_unit,
            is_taxable=is_taxable,
            taxonomy_id=taxonomy_id,
            tags=tags,
            who_made=who_made,
            when_made=when_made,
            state=state,
            is_supply=is_supply,
            production_partner_ids=production_partner_ids,
            type=type,
            ecgt_garan_brand=ecgt_garan_brand,
            ecgt_garan_years=ecgt_garan_years,
            ecgt_garan_model=ecgt_garan_model,
            ecgt_garan_guarantee_details=ecgt_garan_guarantee_details,
            ecgt_other_commercial_guarantee_details=ecgt_other_commercial_guarantee_details,
            ecgt_after_sales_service_info=ecgt_after_sales_service_info,
            ecgt_software_update_details=ecgt_software_update_details,
            gpsr_manufacturer_type=gpsr_manufacturer_type,
            gpsr_manufacturer_id=gpsr_manufacturer_id,
            gpsr_responsible_person_type=gpsr_responsible_person_type,
            gpsr_responsible_person_id=gpsr_responsible_person_id,
            gpsr_serial_number=gpsr_serial_number,
            gpsr_safety_warnings=gpsr_safety_warnings,
        )
