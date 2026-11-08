# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.inventory import models as _models
from ebay_sell.inventory.models.bulk_ebay_offer_details_with_keys import BulkEbayOfferDetailsWithKeys
from ebay_sell.inventory.models.bulk_offer import BulkOffer
from ebay_sell.inventory.models.bulk_offer_response import BulkOfferResponse
from ebay_sell.inventory.models.bulk_publish_response import BulkPublishResponse
from ebay_sell.inventory.models.ebay_offer_details_with_all import EbayOfferDetailsWithAll
from ebay_sell.inventory.models.ebay_offer_details_with_id import EbayOfferDetailsWithId
from ebay_sell.inventory.models.ebay_offer_details_with_keys import EbayOfferDetailsWithKeys
from ebay_sell.inventory.models.error import Error
from ebay_sell.inventory.models.fees_summary_response import FeesSummaryResponse
from ebay_sell.inventory.models.offer_keys_with_id import OfferKeysWithId
from ebay_sell.inventory.models.offer_response import OfferResponse
from ebay_sell.inventory.models.offers import Offers
from ebay_sell.inventory.models.publish_by_inventory_item_group_request import PublishByInventoryItemGroupRequest
from ebay_sell.inventory.models.publish_response import PublishResponse
from ebay_sell.inventory.models.withdraw_by_inventory_item_group_request import WithdrawByInventoryItemGroupRequest
from ebay_sell.inventory.models.withdraw_response import WithdrawResponse

_bulk_create_offer: Operation[BulkOfferResponse] = Operation(
    id="bulkCreateOffer",
    method="POST",
    path="/sell/inventory/v1/bulk_create_offer",
    resource="offers",
    name="bulk_create",
    params=(Param("Content-Language", "content_language", "header"),),
    response=BulkOfferResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_bulk_publish_offer: Operation[BulkPublishResponse] = Operation(
    id="bulkPublishOffer",
    method="POST",
    path="/sell/inventory/v1/bulk_publish_offer",
    resource="offers",
    name="bulk_publish",
    params=(),
    response=BulkPublishResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_create_offer: Operation[OfferResponse] = Operation(
    id="createOffer",
    method="POST",
    path="/sell/inventory/v1/offer",
    resource="offers",
    name="create",
    params=(Param("Content-Language", "content_language", "header"),),
    response=OfferResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_delete_offer: Operation[Error] = Operation(
    id="deleteOffer",
    method="DELETE",
    path="/sell/inventory/v1/offer/{offerId}",
    resource="offers",
    name="delete",
    params=(Param("offerId", "offer_id", "path"),),
    response=Error,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_listing_fees: Operation[FeesSummaryResponse] = Operation(
    id="getListingFees",
    method="POST",
    path="/sell/inventory/v1/offer/get_listing_fees",
    resource="offers",
    name="get_listing_fees",
    params=(),
    response=FeesSummaryResponse,
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
_get_offer: Operation[EbayOfferDetailsWithAll] = Operation(
    id="getOffer",
    method="GET",
    path="/sell/inventory/v1/offer/{offerId}",
    resource="offers",
    name="get",
    params=(Param("offerId", "offer_id", "path"),),
    response=EbayOfferDetailsWithAll,
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
_get_offers: Operation[Offers] = Operation(
    id="getOffers",
    method="GET",
    path="/sell/inventory/v1/offer",
    resource="offers",
    name="list",
    params=(
        Param("format", "format", "query"),
        Param("limit", "limit", "query"),
        Param("marketplace_id", "marketplace_id", "query"),
        Param("offset", "offset", "query"),
        Param("sku", "sku", "query"),
    ),
    response=Offers,
    returns_json=True,
    iterator="iter",
    item=_models.EbayOfferDetailsWithAll,
    paging=NextLink(
        items="offers",
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
_publish_offer: Operation[PublishResponse] = Operation(
    id="publishOffer",
    method="POST",
    path="/sell/inventory/v1/offer/{offerId}/publish",
    resource="offers",
    name="publish",
    params=(Param("offerId", "offer_id", "path"),),
    response=PublishResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_publish_offer_by_inventory_item_group: Operation[PublishResponse] = Operation(
    id="publishOfferByInventoryItemGroup",
    method="POST",
    path="/sell/inventory/v1/offer/publish_by_inventory_item_group",
    resource="offers",
    name="publish_by_inventory_item_group",
    params=(),
    response=PublishResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_update_offer: Operation[OfferResponse] = Operation(
    id="updateOffer",
    method="PUT",
    path="/sell/inventory/v1/offer/{offerId}",
    resource="offers",
    name="update",
    params=(
        Param("offerId", "offer_id", "path"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=OfferResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_withdraw_offer: Operation[WithdrawResponse] = Operation(
    id="withdrawOffer",
    method="POST",
    path="/sell/inventory/v1/offer/{offerId}/withdraw",
    resource="offers",
    name="withdraw",
    params=(Param("offerId", "offer_id", "path"),),
    response=WithdrawResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_withdraw_offer_by_inventory_item_group: Operation[Error] = Operation(
    id="withdrawOfferByInventoryItemGroup",
    method="POST",
    path="/sell/inventory/v1/offer/withdraw_by_inventory_item_group",
    resource="offers",
    name="withdraw_by_inventory_item_group",
    params=(),
    response=Error,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)

OPERATIONS = (
    _bulk_create_offer,
    _bulk_publish_offer,
    _create_offer,
    _delete_offer,
    _get_listing_fees,
    _get_offer,
    _get_offers,
    _publish_offer,
    _publish_offer_by_inventory_item_group,
    _update_offer,
    _withdraw_offer,
    _withdraw_offer_by_inventory_item_group,
)


class OffersApi(Resource):
    @checked
    def bulk_create(
        self,
        body: Union[BulkEbayOfferDetailsWithKeys, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BulkOfferResponse:
        """Create several unpublished offers."""
        return self._call(
            _bulk_create_offer,
            _body=body,
            content_language=content_language,
        )

    @checked
    def bulk_publish(
        self,
        body: Union[BulkOffer, Mapping[str, Any]],
    ) -> BulkPublishResponse:
        """Publish several offers as listings."""
        return self._call(
            _bulk_publish_offer,
            _body=body,
        )

    @checked
    def create(
        self,
        body: Union[EbayOfferDetailsWithKeys, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> OfferResponse:
        """Create an unpublished offer for an inventory item."""
        return self._call(
            _create_offer,
            _body=body,
            content_language=content_language,
        )

    @checked
    def delete(
        self,
        offer_id: StrictStr,
    ) -> Error:
        """Delete an offer"""
        return self._call(
            _delete_offer,
            offer_id=offer_id,
        )

    @checked
    def get_listing_fees(
        self,
        body: Optional[Union[OfferKeysWithId, Mapping[str, Any]]] = None,
    ) -> FeesSummaryResponse:
        """Estimate the listing fees of unpublished offers."""
        return self._call(
            _get_listing_fees,
            _body=body,
        )

    @checked
    def get(
        self,
        offer_id: StrictStr,
    ) -> EbayOfferDetailsWithAll:
        """Get one offer."""
        return self._call(
            _get_offer,
            offer_id=offer_id,
        )

    @checked
    def list(
        self,
        *,
        format: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        marketplace_id: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
    ) -> Offers:
        """List one page of the offers of a SKU."""
        return self._call(
            _get_offers,
            format=format,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            sku=sku,
        )

    @checked
    def iter(
        self,
        *,
        format: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        marketplace_id: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
    ) -> Iterator[_models.EbayOfferDetailsWithAll]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_offers,
            format=format,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            sku=sku,
        )

    @checked
    def publish(
        self,
        offer_id: StrictStr,
    ) -> PublishResponse:
        """Publish an offer as a listing."""
        return self._call(
            _publish_offer,
            offer_id=offer_id,
        )

    @checked
    def publish_by_inventory_item_group(
        self,
        body: Union[PublishByInventoryItemGroupRequest, Mapping[str, Any]],
    ) -> PublishResponse:
        """Publish the offers of an inventory item group as one multi-variation listing."""
        return self._call(
            _publish_offer_by_inventory_item_group,
            _body=body,
        )

    @checked
    def update(
        self,
        offer_id: StrictStr,
        body: Union[EbayOfferDetailsWithId, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> OfferResponse:
        """Replace an offer."""
        return self._call(
            _update_offer,
            offer_id=offer_id,
            _body=body,
            content_language=content_language,
        )

    @checked
    def withdraw(
        self,
        offer_id: StrictStr,
    ) -> WithdrawResponse:
        """End the listing of an offer and keep the offer."""
        return self._call(
            _withdraw_offer,
            offer_id=offer_id,
        )

    @checked
    def withdraw_by_inventory_item_group(
        self,
        body: Union[WithdrawByInventoryItemGroupRequest, Mapping[str, Any]],
    ) -> Error:
        """End the multi-variation listing of an inventory item group."""
        return self._call(
            _withdraw_offer_by_inventory_item_group,
            _body=body,
        )


class AsyncOffersApi(AsyncResource):
    @checked
    async def bulk_create(
        self,
        body: Union[BulkEbayOfferDetailsWithKeys, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> BulkOfferResponse:
        """Create several unpublished offers."""
        return await self._call(
            _bulk_create_offer,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def bulk_publish(
        self,
        body: Union[BulkOffer, Mapping[str, Any]],
    ) -> BulkPublishResponse:
        """Publish several offers as listings."""
        return await self._call(
            _bulk_publish_offer,
            _body=body,
        )

    @checked
    async def create(
        self,
        body: Union[EbayOfferDetailsWithKeys, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> OfferResponse:
        """Create an unpublished offer for an inventory item."""
        return await self._call(
            _create_offer,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def delete(
        self,
        offer_id: StrictStr,
    ) -> Error:
        """Delete an offer"""
        return await self._call(
            _delete_offer,
            offer_id=offer_id,
        )

    @checked
    async def get_listing_fees(
        self,
        body: Optional[Union[OfferKeysWithId, Mapping[str, Any]]] = None,
    ) -> FeesSummaryResponse:
        """Estimate the listing fees of unpublished offers."""
        return await self._call(
            _get_listing_fees,
            _body=body,
        )

    @checked
    async def get(
        self,
        offer_id: StrictStr,
    ) -> EbayOfferDetailsWithAll:
        """Get one offer."""
        return await self._call(
            _get_offer,
            offer_id=offer_id,
        )

    @checked
    async def list(
        self,
        *,
        format: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        marketplace_id: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
    ) -> Offers:
        """List one page of the offers of a SKU."""
        return await self._call(
            _get_offers,
            format=format,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            sku=sku,
        )

    @checked
    def iter(
        self,
        *,
        format: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        marketplace_id: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sku: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.EbayOfferDetailsWithAll]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_offers,
            format=format,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            sku=sku,
        )

    @checked
    async def publish(
        self,
        offer_id: StrictStr,
    ) -> PublishResponse:
        """Publish an offer as a listing."""
        return await self._call(
            _publish_offer,
            offer_id=offer_id,
        )

    @checked
    async def publish_by_inventory_item_group(
        self,
        body: Union[PublishByInventoryItemGroupRequest, Mapping[str, Any]],
    ) -> PublishResponse:
        """Publish the offers of an inventory item group as one multi-variation listing."""
        return await self._call(
            _publish_offer_by_inventory_item_group,
            _body=body,
        )

    @checked
    async def update(
        self,
        offer_id: StrictStr,
        body: Union[EbayOfferDetailsWithId, Mapping[str, Any]],
        *,
        content_language: Optional[StrictStr] = None,
    ) -> OfferResponse:
        """Replace an offer."""
        return await self._call(
            _update_offer,
            offer_id=offer_id,
            _body=body,
            content_language=content_language,
        )

    @checked
    async def withdraw(
        self,
        offer_id: StrictStr,
    ) -> WithdrawResponse:
        """End the listing of an offer and keep the offer."""
        return await self._call(
            _withdraw_offer,
            offer_id=offer_id,
        )

    @checked
    async def withdraw_by_inventory_item_group(
        self,
        body: Union[WithdrawByInventoryItemGroupRequest, Mapping[str, Any]],
    ) -> Error:
        """End the multi-variation listing of an inventory item group."""
        return await self._call(
            _withdraw_offer_by_inventory_item_group,
            _body=body,
        )
