# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.ad_group import AdGroup
from ebay_sell.marketing.models.ad_group_paged_collection_response import AdGroupPagedCollectionResponse
from ebay_sell.marketing.models.create_ad_group_request import CreateAdGroupRequest
from ebay_sell.marketing.models.error import Error
from ebay_sell.marketing.models.targeted_bid_request import TargetedBidRequest
from ebay_sell.marketing.models.targeted_bids_paged_collection import TargetedBidsPagedCollection
from ebay_sell.marketing.models.targeted_keyword_request import TargetedKeywordRequest
from ebay_sell.marketing.models.targeted_keywords_paged_collection import TargetedKeywordsPagedCollection
from ebay_sell.marketing.models.update_ad_group_request import UpdateAdGroupRequest

_create_ad_group: Operation[object] = Operation(
    id="createAdGroup",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group",
    resource="ad_groups",
    name="create",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_ad_group: Operation[AdGroup] = Operation(
    id="getAdGroup",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}",
    resource="ad_groups",
    name="get",
    params=(
        Param("ad_group_id", "ad_group_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=AdGroup,
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
_get_ad_groups: Operation[AdGroupPagedCollectionResponse] = Operation(
    id="getAdGroups",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group",
    resource="ad_groups",
    name="list",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("ad_group_status", "ad_group_status", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=AdGroupPagedCollectionResponse,
    returns_json=True,
    iterator="iter",
    item=_models.AdGroup,
    paging=NextLink(
        items="adGroups",
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
_suggest_bids: Operation[TargetedBidsPagedCollection] = Operation(
    id="suggestBids",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids",
    resource="ad_groups",
    name="suggest_bids",
    params=(
        Param("ad_group_id", "ad_group_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=TargetedBidsPagedCollection,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_suggest_keywords: Operation[TargetedKeywordsPagedCollection] = Operation(
    id="suggestKeywords",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_keywords",
    resource="ad_groups",
    name="suggest_keywords",
    params=(
        Param("ad_group_id", "ad_group_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=TargetedKeywordsPagedCollection,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_ad_group: Operation[Error] = Operation(
    id="updateAdGroup",
    method="PUT",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}",
    resource="ad_groups",
    name="update",
    params=(
        Param("ad_group_id", "ad_group_id", "path"),
        Param("campaign_id", "campaign_id", "path"),
    ),
    response=Error,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _create_ad_group,
    _get_ad_group,
    _get_ad_groups,
    _suggest_bids,
    _suggest_keywords,
    _update_ad_group,
)


class AdGroupsApi(Resource):
    @checked
    def create(
        self,
        campaign_id: StrictStr,
        body: Union[CreateAdGroupRequest, Mapping[str, Any]],
    ) -> object:
        """Create an ad group in a campaign."""
        return self._call(
            _create_ad_group,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def get(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
    ) -> AdGroup:
        """Get one ad group."""
        return self._call(
            _get_ad_group,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
        )

    @checked
    def list(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AdGroupPagedCollectionResponse:
        """List one page of a campaign's ad groups."""
        return self._call(
            _get_ad_groups,
            campaign_id=campaign_id,
            ad_group_status=ad_group_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.AdGroup]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ad_groups,
            campaign_id=campaign_id,
            ad_group_status=ad_group_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def suggest_bids(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
        body: Union[TargetedBidRequest, Mapping[str, Any]],
    ) -> TargetedBidsPagedCollection:
        """Suggest bids for keywords in an ad group."""
        return self._call(
            _suggest_bids,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def suggest_keywords(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
        body: Optional[Union[TargetedKeywordRequest, Mapping[str, Any]]] = None,
    ) -> TargetedKeywordsPagedCollection:
        """Suggest keywords for an ad group."""
        return self._call(
            _suggest_keywords,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def update(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
        body: Union[UpdateAdGroupRequest, Mapping[str, Any]],
    ) -> Error:
        """Update an ad group."""
        return self._call(
            _update_ad_group,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
            _body=body,
        )


class AsyncAdGroupsApi(AsyncResource):
    @checked
    async def create(
        self,
        campaign_id: StrictStr,
        body: Union[CreateAdGroupRequest, Mapping[str, Any]],
    ) -> object:
        """Create an ad group in a campaign."""
        return await self._call(
            _create_ad_group,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def get(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
    ) -> AdGroup:
        """Get one ad group."""
        return await self._call(
            _get_ad_group,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
        )

    @checked
    async def list(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AdGroupPagedCollectionResponse:
        """List one page of a campaign's ad groups."""
        return await self._call(
            _get_ad_groups,
            campaign_id=campaign_id,
            ad_group_status=ad_group_status,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        campaign_id: StrictStr,
        *,
        ad_group_status: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.AdGroup]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ad_groups,
            campaign_id=campaign_id,
            ad_group_status=ad_group_status,
            limit=limit,
            offset=offset,
        )

    @checked
    async def suggest_bids(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
        body: Union[TargetedBidRequest, Mapping[str, Any]],
    ) -> TargetedBidsPagedCollection:
        """Suggest bids for keywords in an ad group."""
        return await self._call(
            _suggest_bids,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def suggest_keywords(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
        body: Optional[Union[TargetedKeywordRequest, Mapping[str, Any]]] = None,
    ) -> TargetedKeywordsPagedCollection:
        """Suggest keywords for an ad group."""
        return await self._call(
            _suggest_keywords,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def update(
        self,
        ad_group_id: StrictStr,
        campaign_id: StrictStr,
        body: Union[UpdateAdGroupRequest, Mapping[str, Any]],
    ) -> Error:
        """Update an ad group."""
        return await self._call(
            _update_ad_group,
            ad_group_id=ad_group_id,
            campaign_id=campaign_id,
            _body=body,
        )
