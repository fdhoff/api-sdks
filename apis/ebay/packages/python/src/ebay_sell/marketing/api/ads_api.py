# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.ad import Ad
from ebay_sell.marketing.models.ad_ids import AdIds
from ebay_sell.marketing.models.ad_paged_collection_response import AdPagedCollectionResponse
from ebay_sell.marketing.models.ad_references import AdReferences
from ebay_sell.marketing.models.ads import Ads
from ebay_sell.marketing.models.bulk_ad_response import BulkAdResponse
from ebay_sell.marketing.models.bulk_ad_update_response import BulkAdUpdateResponse
from ebay_sell.marketing.models.bulk_ad_update_status_by_listing_id_response import (
    BulkAdUpdateStatusByListingIdResponse,
)
from ebay_sell.marketing.models.bulk_ad_update_status_response import BulkAdUpdateStatusResponse
from ebay_sell.marketing.models.bulk_create_ad_request import BulkCreateAdRequest
from ebay_sell.marketing.models.bulk_create_ads_by_inventory_reference_request import (
    BulkCreateAdsByInventoryReferenceRequest,
)
from ebay_sell.marketing.models.bulk_create_ads_by_inventory_reference_response import (
    BulkCreateAdsByInventoryReferenceResponse,
)
from ebay_sell.marketing.models.bulk_delete_ad_request import BulkDeleteAdRequest
from ebay_sell.marketing.models.bulk_delete_ad_response import BulkDeleteAdResponse
from ebay_sell.marketing.models.bulk_delete_ads_by_inventory_reference_request import (
    BulkDeleteAdsByInventoryReferenceRequest,
)
from ebay_sell.marketing.models.bulk_delete_ads_by_inventory_reference_response import (
    BulkDeleteAdsByInventoryReferenceResponse,
)
from ebay_sell.marketing.models.bulk_update_ad_status_by_listing_id_request import BulkUpdateAdStatusByListingIdRequest
from ebay_sell.marketing.models.bulk_update_ad_status_request import BulkUpdateAdStatusRequest
from ebay_sell.marketing.models.bulk_update_ads_by_inventory_reference_response import (
    BulkUpdateAdsByInventoryReferenceResponse,
)
from ebay_sell.marketing.models.create_ad_request import CreateAdRequest
from ebay_sell.marketing.models.create_ads_by_inventory_reference_request import CreateAdsByInventoryReferenceRequest
from ebay_sell.marketing.models.delete_ads_by_inventory_reference_request import DeleteAdsByInventoryReferenceRequest
from ebay_sell.marketing.models.update_bid_percentage_request import UpdateBidPercentageRequest

_bulk_create_ads_by_inventory_reference: Operation[BulkCreateAdsByInventoryReferenceResponse] = Operation(
    id="bulkCreateAdsByInventoryReference",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
    resource="ads",
    name="bulk_create_by_inventory_reference",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkCreateAdsByInventoryReferenceResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_create_ads_by_listing_id: Operation[BulkAdResponse] = Operation(
    id="bulkCreateAdsByListingId",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id",
    resource="ads",
    name="bulk_create_by_listing_id",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkAdResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_delete_ads_by_inventory_reference: Operation[BulkDeleteAdsByInventoryReferenceResponse] = Operation(
    id="bulkDeleteAdsByInventoryReference",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference",
    resource="ads",
    name="bulk_delete_by_inventory_reference",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkDeleteAdsByInventoryReferenceResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_delete_ads_by_listing_id: Operation[BulkDeleteAdResponse] = Operation(
    id="bulkDeleteAdsByListingId",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id",
    resource="ads",
    name="bulk_delete_by_listing_id",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkDeleteAdResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_update_ads_bid_by_inventory_reference: Operation[BulkUpdateAdsByInventoryReferenceResponse] = Operation(
    id="bulkUpdateAdsBidByInventoryReference",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference",
    resource="ads",
    name="bulk_update_bid_by_inventory_reference",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkUpdateAdsByInventoryReferenceResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_update_ads_bid_by_listing_id: Operation[BulkAdUpdateResponse] = Operation(
    id="bulkUpdateAdsBidByListingId",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id",
    resource="ads",
    name="bulk_update_bid_by_listing_id",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkAdUpdateResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_update_ads_status: Operation[BulkAdUpdateStatusResponse] = Operation(
    id="bulkUpdateAdsStatus",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status",
    resource="ads",
    name="bulk_update_status",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkAdUpdateStatusResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_bulk_update_ads_status_by_listing_id: Operation[BulkAdUpdateStatusByListingIdResponse] = Operation(
    id="bulkUpdateAdsStatusByListingId",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id",
    resource="ads",
    name="bulk_update_status_by_listing_id",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=BulkAdUpdateStatusByListingIdResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_create_ad_by_listing_id: Operation[object] = Operation(
    id="createAdByListingId",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad",
    resource="ads",
    name="create_by_listing_id",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_create_ads_by_inventory_reference: Operation[AdReferences] = Operation(
    id="createAdsByInventoryReference",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_inventory_reference",
    resource="ads",
    name="create_by_inventory_reference",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=AdReferences,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_ad: Operation[None] = Operation(
    id="deleteAd",
    method="DELETE",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}",
    resource="ads",
    name="delete",
    params=(
        Param("ad_id", "ad_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_ads_by_inventory_reference: Operation[AdIds] = Operation(
    id="deleteAdsByInventoryReference",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/delete_ads_by_inventory_reference",
    resource="ads",
    name="delete_by_inventory_reference",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=AdIds,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_ad: Operation[Ad] = Operation(
    id="getAd",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}",
    resource="ads",
    name="get",
    params=(
        Param("ad_id", "ad_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=Ad,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_get_ads: Operation[AdPagedCollectionResponse] = Operation(
    id="getAds",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad",
    resource="ads",
    name="list",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("ad_group_ids", "ad_group_ids", "query"),
        Param("ad_status", "ad_status", "query"),
        Param("limit", "limit", "query"),
        Param("listing_ids", "listing_ids", "query"),
        Param("offset", "offset", "query"),
    ),
    response=AdPagedCollectionResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Ad,
    paging=NextLink(
        items="ads",
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
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_get_ads_by_inventory_reference: Operation[Ads] = Operation(
    id="getAdsByInventoryReference",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/get_ads_by_inventory_reference",
    resource="ads",
    name="get_by_inventory_reference",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("inventory_reference_id", "inventory_reference_id", "query"),
        Param("inventory_reference_type", "inventory_reference_type", "query"),
    ),
    response=Ads,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_update_bid: Operation[None] = Operation(
    id="updateBid",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid",
    resource="ads",
    name="update_bid",
    params=(
        Param("ad_id", "ad_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _bulk_create_ads_by_inventory_reference,
    _bulk_create_ads_by_listing_id,
    _bulk_delete_ads_by_inventory_reference,
    _bulk_delete_ads_by_listing_id,
    _bulk_update_ads_bid_by_inventory_reference,
    _bulk_update_ads_bid_by_listing_id,
    _bulk_update_ads_status,
    _bulk_update_ads_status_by_listing_id,
    _create_ad_by_listing_id,
    _create_ads_by_inventory_reference,
    _delete_ad,
    _delete_ads_by_inventory_reference,
    _get_ad,
    _get_ads,
    _get_ads_by_inventory_reference,
    _update_bid,
)


class AdsApi(Resource):
    @checked
    def bulk_create_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> BulkCreateAdsByInventoryReferenceResponse:
        """Create ads for several inventory references."""
        return self._call(
            _bulk_create_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_create_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdRequest, Mapping[str, Any]],
    ) -> BulkAdResponse:
        """Create ads for several listings."""
        return self._call(
            _bulk_create_ads_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_delete_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[BulkDeleteAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> BulkDeleteAdsByInventoryReferenceResponse:
        """Delete the ads of several inventory references."""
        return self._call(
            _bulk_delete_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_delete_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkDeleteAdRequest, Mapping[str, Any]],
    ) -> BulkDeleteAdResponse:
        """Delete the ads of several listings."""
        return self._call(
            _bulk_delete_ads_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_update_bid_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> BulkUpdateAdsByInventoryReferenceResponse:
        """Change the bids of several inventory references' ads."""
        return self._call(
            _bulk_update_ads_bid_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_update_bid_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdRequest, Mapping[str, Any]],
    ) -> BulkAdUpdateResponse:
        """Change the bids of several listings' ads."""
        return self._call(
            _bulk_update_ads_bid_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_update_status(
        self,
        campaign_id: StrictStr,
        body: Union[BulkUpdateAdStatusRequest, Mapping[str, Any]],
    ) -> BulkAdUpdateStatusResponse:
        """Change the status of several ads."""
        return self._call(
            _bulk_update_ads_status,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def bulk_update_status_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkUpdateAdStatusByListingIdRequest, Mapping[str, Any]],
    ) -> BulkAdUpdateStatusByListingIdResponse:
        """Change the status of several listings' ads."""
        return self._call(
            _bulk_update_ads_status_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def create_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[CreateAdRequest, Mapping[str, Any]],
    ) -> object:
        """Create an ad for a listing."""
        return self._call(
            _create_ad_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def create_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[CreateAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> AdReferences:
        """Create ads for an inventory reference."""
        return self._call(
            _create_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def delete(
        self,
        ad_id: StrictStr,
        campaign_id: StrictStr,
    ) -> None:
        """Delete an ad."""
        return self._call(
            _delete_ad,
            ad_id=ad_id,
            campaign_id=campaign_id,
        )

    @checked
    def delete_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[DeleteAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> AdIds:
        """Delete a campaign's ads for one inventory reference."""
        return self._call(
            _delete_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def get(
        self,
        ad_id: StrictStr,
        campaign_id: StrictStr,
    ) -> Ad:
        """Get one ad."""
        return self._call(
            _get_ad,
            ad_id=ad_id,
            campaign_id=campaign_id,
        )

    @checked
    def list(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        ad_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        listing_ids: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AdPagedCollectionResponse:
        """List one page of a campaign's ads."""
        return self._call(
            _get_ads,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            ad_status=ad_status,
            limit=limit,
            listing_ids=listing_ids,
            offset=offset,
        )

    @checked
    def iter(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        ad_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        listing_ids: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.Ad]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ads,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            ad_status=ad_status,
            limit=limit,
            listing_ids=listing_ids,
            offset=offset,
        )

    @checked
    def get_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        *,
        inventory_reference_id: StrictStr,
        inventory_reference_type: StrictStr,
    ) -> Ads:
        """Get a campaign's ads for one inventory reference."""
        return self._call(
            _get_ads_by_inventory_reference,
            campaign_id=campaign_id,
            inventory_reference_id=inventory_reference_id,
            inventory_reference_type=inventory_reference_type,
        )

    @checked
    def update_bid(
        self,
        ad_id: StrictStr,
        campaign_id: StrictStr,
        body: Union[UpdateBidPercentageRequest, Mapping[str, Any]],
    ) -> None:
        """Change the bid of an ad."""
        return self._call(
            _update_bid,
            ad_id=ad_id,
            campaign_id=campaign_id,
            _body=body,
        )


class AsyncAdsApi(AsyncResource):
    @checked
    async def bulk_create_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> BulkCreateAdsByInventoryReferenceResponse:
        """Create ads for several inventory references."""
        return await self._call(
            _bulk_create_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_create_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdRequest, Mapping[str, Any]],
    ) -> BulkAdResponse:
        """Create ads for several listings."""
        return await self._call(
            _bulk_create_ads_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_delete_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[BulkDeleteAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> BulkDeleteAdsByInventoryReferenceResponse:
        """Delete the ads of several inventory references."""
        return await self._call(
            _bulk_delete_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_delete_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkDeleteAdRequest, Mapping[str, Any]],
    ) -> BulkDeleteAdResponse:
        """Delete the ads of several listings."""
        return await self._call(
            _bulk_delete_ads_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_update_bid_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> BulkUpdateAdsByInventoryReferenceResponse:
        """Change the bids of several inventory references' ads."""
        return await self._call(
            _bulk_update_ads_bid_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_update_bid_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkCreateAdRequest, Mapping[str, Any]],
    ) -> BulkAdUpdateResponse:
        """Change the bids of several listings' ads."""
        return await self._call(
            _bulk_update_ads_bid_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_update_status(
        self,
        campaign_id: StrictStr,
        body: Union[BulkUpdateAdStatusRequest, Mapping[str, Any]],
    ) -> BulkAdUpdateStatusResponse:
        """Change the status of several ads."""
        return await self._call(
            _bulk_update_ads_status,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def bulk_update_status_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[BulkUpdateAdStatusByListingIdRequest, Mapping[str, Any]],
    ) -> BulkAdUpdateStatusByListingIdResponse:
        """Change the status of several listings' ads."""
        return await self._call(
            _bulk_update_ads_status_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def create_by_listing_id(
        self,
        campaign_id: StrictStr,
        body: Union[CreateAdRequest, Mapping[str, Any]],
    ) -> object:
        """Create an ad for a listing."""
        return await self._call(
            _create_ad_by_listing_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def create_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[CreateAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> AdReferences:
        """Create ads for an inventory reference."""
        return await self._call(
            _create_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def delete(
        self,
        ad_id: StrictStr,
        campaign_id: StrictStr,
    ) -> None:
        """Delete an ad."""
        return await self._call(
            _delete_ad,
            ad_id=ad_id,
            campaign_id=campaign_id,
        )

    @checked
    async def delete_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        body: Union[DeleteAdsByInventoryReferenceRequest, Mapping[str, Any]],
    ) -> AdIds:
        """Delete a campaign's ads for one inventory reference."""
        return await self._call(
            _delete_ads_by_inventory_reference,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def get(
        self,
        ad_id: StrictStr,
        campaign_id: StrictStr,
    ) -> Ad:
        """Get one ad."""
        return await self._call(
            _get_ad,
            ad_id=ad_id,
            campaign_id=campaign_id,
        )

    @checked
    async def list(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        ad_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        listing_ids: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AdPagedCollectionResponse:
        """List one page of a campaign's ads."""
        return await self._call(
            _get_ads,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            ad_status=ad_status,
            limit=limit,
            listing_ids=listing_ids,
            offset=offset,
        )

    @checked
    def iter(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_ids: Optional[StrictStr] = None,
        ad_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        listing_ids: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Ad]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ads,
            campaign_id=campaign_id,
            ad_group_ids=ad_group_ids,
            ad_status=ad_status,
            limit=limit,
            listing_ids=listing_ids,
            offset=offset,
        )

    @checked
    async def get_by_inventory_reference(
        self,
        campaign_id: StrictStr,
        *,
        inventory_reference_id: StrictStr,
        inventory_reference_type: StrictStr,
    ) -> Ads:
        """Get a campaign's ads for one inventory reference."""
        return await self._call(
            _get_ads_by_inventory_reference,
            campaign_id=campaign_id,
            inventory_reference_id=inventory_reference_id,
            inventory_reference_type=inventory_reference_type,
        )

    @checked
    async def update_bid(
        self,
        ad_id: StrictStr,
        campaign_id: StrictStr,
        body: Union[UpdateBidPercentageRequest, Mapping[str, Any]],
    ) -> None:
        """Change the bid of an ad."""
        return await self._call(
            _update_bid,
            ad_id=ad_id,
            campaign_id=campaign_id,
            _body=body,
        )
