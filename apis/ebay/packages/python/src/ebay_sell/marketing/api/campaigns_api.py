# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.campaign import Campaign
from ebay_sell.marketing.models.campaign_paged_collection_response import CampaignPagedCollectionResponse
from ebay_sell.marketing.models.campaigns import Campaigns
from ebay_sell.marketing.models.clone_campaign_request import CloneCampaignRequest
from ebay_sell.marketing.models.create_campaign_request import CreateCampaignRequest
from ebay_sell.marketing.models.suggest_budget_response import SuggestBudgetResponse
from ebay_sell.marketing.models.suggest_max_cpc_request import SuggestMaxCpcRequest
from ebay_sell.marketing.models.suggest_max_cpc_response import SuggestMaxCpcResponse
from ebay_sell.marketing.models.targeted_ads_paged_collection import TargetedAdsPagedCollection
from ebay_sell.marketing.models.update_adrate_strategy_request import UpdateAdrateStrategyRequest
from ebay_sell.marketing.models.update_bidding_strategy_request import UpdateBiddingStrategyRequest
from ebay_sell.marketing.models.update_campaign_budget_request import UpdateCampaignBudgetRequest
from ebay_sell.marketing.models.update_campaign_identification_request import UpdateCampaignIdentificationRequest

_clone_campaign: Operation[object] = Operation(
    id="cloneCampaign",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/clone",
    resource="campaigns",
    name="clone",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_create_campaign: Operation[object] = Operation(
    id="createCampaign",
    method="POST",
    path="/sell/marketing/v1/ad_campaign",
    resource="campaigns",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_campaign: Operation[None] = Operation(
    id="deleteCampaign",
    method="DELETE",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}",
    resource="campaigns",
    name="delete",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_end_campaign: Operation[None] = Operation(
    id="endCampaign",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/end",
    resource="campaigns",
    name="end",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_find_campaign_by_ad_reference: Operation[Campaigns] = Operation(
    id="findCampaignByAdReference",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/find_campaign_by_ad_reference",
    resource="campaigns",
    name="find_by_ad_reference",
    params=(
        Param("inventory_reference_id", "inventory_reference_id", "query"),
        Param("inventory_reference_type", "inventory_reference_type", "query"),
        Param("listing_id", "listing_id", "query"),
    ),
    response=Campaigns,
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
_get_campaign: Operation[Campaign] = Operation(
    id="getCampaign",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}",
    resource="campaigns",
    name="get",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=Campaign,
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
_get_campaign_by_name: Operation[Campaign] = Operation(
    id="getCampaignByName",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/get_campaign_by_name",
    resource="campaigns",
    name="get_by_name",
    params=(Param("campaign_name", "campaign_name", "query"),),
    response=Campaign,
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
_get_campaigns: Operation[CampaignPagedCollectionResponse] = Operation(
    id="getCampaigns",
    method="GET",
    path="/sell/marketing/v1/ad_campaign",
    resource="campaigns",
    name="list",
    params=(
        Param("campaign_name", "campaign_name", "query"),
        Param("campaign_status", "campaign_status", "query"),
        Param("campaign_targeting_types", "campaign_targeting_types", "query"),
        Param("channels", "channels", "query"),
        Param("end_date_range", "end_date_range", "query"),
        Param("funding_strategy", "funding_strategy", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("start_date_range", "start_date_range", "query"),
    ),
    response=CampaignPagedCollectionResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Campaign,
    paging=NextLink(
        items="campaigns",
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
_pause_campaign: Operation[None] = Operation(
    id="pauseCampaign",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/pause",
    resource="campaigns",
    name="pause",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_resume_campaign: Operation[None] = Operation(
    id="resumeCampaign",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/resume",
    resource="campaigns",
    name="resume",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_suggest_budget: Operation[SuggestBudgetResponse] = Operation(
    id="suggestBudget",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/suggest_budget",
    resource="campaigns",
    name="suggest_budget",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=SuggestBudgetResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_suggest_items: Operation[TargetedAdsPagedCollection] = Operation(
    id="suggestItems",
    method="GET",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/suggest_items",
    resource="campaigns",
    name="suggest_items",
    params=(
        Param("campaign_id", "campaign_id", "path"),
        Param("category_ids", "category_ids", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=TargetedAdsPagedCollection,
    returns_json=True,
    iterator="iter_suggested_items",
    item=_models.TargetingItems,
    paging=NextLink(
        items="suggestedItems",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_suggest_max_cpc: Operation[SuggestMaxCpcResponse] = Operation(
    id="suggestMaxCpc",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/suggest_max_cpc",
    resource="campaigns",
    name="suggest_max_cpc",
    params=(),
    response=SuggestMaxCpcResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_ad_rate_strategy: Operation[None] = Operation(
    id="updateAdRateStrategy",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/update_ad_rate_strategy",
    resource="campaigns",
    name="update_ad_rate_strategy",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_bidding_strategy: Operation[None] = Operation(
    id="updateBiddingStrategy",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/update_bidding_strategy",
    resource="campaigns",
    name="update_bidding_strategy",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_campaign_budget: Operation[object] = Operation(
    id="updateCampaignBudget",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_budget",
    resource="campaigns",
    name="update_budget",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_campaign_identification: Operation[None] = Operation(
    id="updateCampaignIdentification",
    method="POST",
    path="/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_identification",
    resource="campaigns",
    name="update_identification",
    params=(Param("campaign_id", "campaign_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _clone_campaign,
    _create_campaign,
    _delete_campaign,
    _end_campaign,
    _find_campaign_by_ad_reference,
    _get_campaign,
    _get_campaign_by_name,
    _get_campaigns,
    _pause_campaign,
    _resume_campaign,
    _suggest_budget,
    _suggest_items,
    _suggest_max_cpc,
    _update_ad_rate_strategy,
    _update_bidding_strategy,
    _update_campaign_budget,
    _update_campaign_identification,
)


class CampaignsApi(Resource):
    @checked
    def clone(
        self,
        campaign_id: StrictStr,
        body: Union[CloneCampaignRequest, Mapping[str, Any]],
    ) -> object:
        """Copy an ended campaign into a new one."""
        return self._call(
            _clone_campaign,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def create(
        self,
        body: Union[CreateCampaignRequest, Mapping[str, Any]],
    ) -> object:
        """Create a Promoted Listings campaign."""
        return self._call(
            _create_campaign,
            _body=body,
        )

    @checked
    def delete(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """Delete a campaign."""
        return self._call(
            _delete_campaign,
            campaign_id=campaign_id,
        )

    @checked
    def end(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """End a campaign."""
        return self._call(
            _end_campaign,
            campaign_id=campaign_id,
        )

    @checked
    def find_by_ad_reference(
        self,
        *,
        inventory_reference_id: Optional[StrictStr] = None,
        inventory_reference_type: Optional[StrictStr] = None,
        listing_id: Optional[StrictStr] = None,
    ) -> Campaigns:
        """Find the campaigns that hold a listing or inventory reference."""
        return self._call(
            _find_campaign_by_ad_reference,
            inventory_reference_id=inventory_reference_id,
            inventory_reference_type=inventory_reference_type,
            listing_id=listing_id,
        )

    @checked
    def get(
        self,
        campaign_id: StrictStr,
    ) -> Campaign:
        """Get one campaign."""
        return self._call(
            _get_campaign,
            campaign_id=campaign_id,
        )

    @checked
    def get_by_name(
        self,
        *,
        campaign_name: StrictStr,
    ) -> Campaign:
        """Get a campaign by its name."""
        return self._call(
            _get_campaign_by_name,
            campaign_name=campaign_name,
        )

    @checked
    def list(
        self,
        *,
        campaign_name: Optional[StrictStr] = None,
        campaign_status: Optional[StrictStr] = None,
        campaign_targeting_types: Optional[StrictStr] = None,
        channels: Optional[StrictStr] = None,
        end_date_range: Optional[StrictStr] = None,
        funding_strategy: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        start_date_range: Optional[StrictStr] = None,
    ) -> CampaignPagedCollectionResponse:
        """List one page of the seller's Promoted Listings campaigns."""
        return self._call(
            _get_campaigns,
            campaign_name=campaign_name,
            campaign_status=campaign_status,
            campaign_targeting_types=campaign_targeting_types,
            channels=channels,
            end_date_range=end_date_range,
            funding_strategy=funding_strategy,
            limit=limit,
            offset=offset,
            start_date_range=start_date_range,
        )

    @checked
    def iter(
        self,
        *,
        campaign_name: Optional[StrictStr] = None,
        campaign_status: Optional[StrictStr] = None,
        campaign_targeting_types: Optional[StrictStr] = None,
        channels: Optional[StrictStr] = None,
        end_date_range: Optional[StrictStr] = None,
        funding_strategy: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        start_date_range: Optional[StrictStr] = None,
    ) -> Iterator[_models.Campaign]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_campaigns,
            campaign_name=campaign_name,
            campaign_status=campaign_status,
            campaign_targeting_types=campaign_targeting_types,
            channels=channels,
            end_date_range=end_date_range,
            funding_strategy=funding_strategy,
            limit=limit,
            offset=offset,
            start_date_range=start_date_range,
        )

    @checked
    def pause(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """Pause a campaign."""
        return self._call(
            _pause_campaign,
            campaign_id=campaign_id,
        )

    @checked
    def resume(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """Resume a paused campaign."""
        return self._call(
            _resume_campaign,
            campaign_id=campaign_id,
        )

    @checked
    def suggest_budget(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SuggestBudgetResponse:
        """Suggest a daily budget for a new campaign."""
        return self._call(
            _suggest_budget,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def suggest_items(
        self,
        campaign_id: StrictStr,
        *,
        category_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> TargetedAdsPagedCollection:
        """List one page of listings suggested for a campaign."""
        return self._call(
            _suggest_items,
            campaign_id=campaign_id,
            category_ids=category_ids,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_suggested_items(
        self,
        campaign_id: StrictStr,
        *,
        category_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.TargetingItems]:
        """Iterate every item across all pages."""
        return self._paginate(
            _suggest_items,
            campaign_id=campaign_id,
            category_ids=category_ids,
            limit=limit,
            offset=offset,
        )

    @checked
    def suggest_max_cpc(
        self,
        body: Union[SuggestMaxCpcRequest, Mapping[str, Any]],
    ) -> SuggestMaxCpcResponse:
        """Suggest a maximum cost per click for a campaign."""
        return self._call(
            _suggest_max_cpc,
            _body=body,
        )

    @checked
    def update_ad_rate_strategy(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateAdrateStrategyRequest, Mapping[str, Any]],
    ) -> None:
        """Change how a campaign sets its ad rates."""
        return self._call(
            _update_ad_rate_strategy,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def update_bidding_strategy(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateBiddingStrategyRequest, Mapping[str, Any]],
    ) -> None:
        """Change the bidding strategy of a campaign."""
        return self._call(
            _update_bidding_strategy,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def update_budget(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateCampaignBudgetRequest, Mapping[str, Any]],
    ) -> object:
        """Change the daily budget of a campaign."""
        return self._call(
            _update_campaign_budget,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    def update_identification(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateCampaignIdentificationRequest, Mapping[str, Any]],
    ) -> None:
        """Rename a campaign or change its dates."""
        return self._call(
            _update_campaign_identification,
            campaign_id=campaign_id,
            _body=body,
        )


class AsyncCampaignsApi(AsyncResource):
    @checked
    async def clone(
        self,
        campaign_id: StrictStr,
        body: Union[CloneCampaignRequest, Mapping[str, Any]],
    ) -> object:
        """Copy an ended campaign into a new one."""
        return await self._call(
            _clone_campaign,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def create(
        self,
        body: Union[CreateCampaignRequest, Mapping[str, Any]],
    ) -> object:
        """Create a Promoted Listings campaign."""
        return await self._call(
            _create_campaign,
            _body=body,
        )

    @checked
    async def delete(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """Delete a campaign."""
        return await self._call(
            _delete_campaign,
            campaign_id=campaign_id,
        )

    @checked
    async def end(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """End a campaign."""
        return await self._call(
            _end_campaign,
            campaign_id=campaign_id,
        )

    @checked
    async def find_by_ad_reference(
        self,
        *,
        inventory_reference_id: Optional[StrictStr] = None,
        inventory_reference_type: Optional[StrictStr] = None,
        listing_id: Optional[StrictStr] = None,
    ) -> Campaigns:
        """Find the campaigns that hold a listing or inventory reference."""
        return await self._call(
            _find_campaign_by_ad_reference,
            inventory_reference_id=inventory_reference_id,
            inventory_reference_type=inventory_reference_type,
            listing_id=listing_id,
        )

    @checked
    async def get(
        self,
        campaign_id: StrictStr,
    ) -> Campaign:
        """Get one campaign."""
        return await self._call(
            _get_campaign,
            campaign_id=campaign_id,
        )

    @checked
    async def get_by_name(
        self,
        *,
        campaign_name: StrictStr,
    ) -> Campaign:
        """Get a campaign by its name."""
        return await self._call(
            _get_campaign_by_name,
            campaign_name=campaign_name,
        )

    @checked
    async def list(
        self,
        *,
        campaign_name: Optional[StrictStr] = None,
        campaign_status: Optional[StrictStr] = None,
        campaign_targeting_types: Optional[StrictStr] = None,
        channels: Optional[StrictStr] = None,
        end_date_range: Optional[StrictStr] = None,
        funding_strategy: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        start_date_range: Optional[StrictStr] = None,
    ) -> CampaignPagedCollectionResponse:
        """List one page of the seller's Promoted Listings campaigns."""
        return await self._call(
            _get_campaigns,
            campaign_name=campaign_name,
            campaign_status=campaign_status,
            campaign_targeting_types=campaign_targeting_types,
            channels=channels,
            end_date_range=end_date_range,
            funding_strategy=funding_strategy,
            limit=limit,
            offset=offset,
            start_date_range=start_date_range,
        )

    @checked
    def iter(
        self,
        *,
        campaign_name: Optional[StrictStr] = None,
        campaign_status: Optional[StrictStr] = None,
        campaign_targeting_types: Optional[StrictStr] = None,
        channels: Optional[StrictStr] = None,
        end_date_range: Optional[StrictStr] = None,
        funding_strategy: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        start_date_range: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Campaign]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_campaigns,
            campaign_name=campaign_name,
            campaign_status=campaign_status,
            campaign_targeting_types=campaign_targeting_types,
            channels=channels,
            end_date_range=end_date_range,
            funding_strategy=funding_strategy,
            limit=limit,
            offset=offset,
            start_date_range=start_date_range,
        )

    @checked
    async def pause(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """Pause a campaign."""
        return await self._call(
            _pause_campaign,
            campaign_id=campaign_id,
        )

    @checked
    async def resume(
        self,
        campaign_id: StrictStr,
    ) -> None:
        """Resume a paused campaign."""
        return await self._call(
            _resume_campaign,
            campaign_id=campaign_id,
        )

    @checked
    async def suggest_budget(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SuggestBudgetResponse:
        """Suggest a daily budget for a new campaign."""
        return await self._call(
            _suggest_budget,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def suggest_items(
        self,
        campaign_id: StrictStr,
        *,
        category_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> TargetedAdsPagedCollection:
        """List one page of listings suggested for a campaign."""
        return await self._call(
            _suggest_items,
            campaign_id=campaign_id,
            category_ids=category_ids,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_suggested_items(
        self,
        campaign_id: StrictStr,
        *,
        category_ids: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.TargetingItems]:
        """Iterate every item across all pages."""
        return self._paginate(
            _suggest_items,
            campaign_id=campaign_id,
            category_ids=category_ids,
            limit=limit,
            offset=offset,
        )

    @checked
    async def suggest_max_cpc(
        self,
        body: Union[SuggestMaxCpcRequest, Mapping[str, Any]],
    ) -> SuggestMaxCpcResponse:
        """Suggest a maximum cost per click for a campaign."""
        return await self._call(
            _suggest_max_cpc,
            _body=body,
        )

    @checked
    async def update_ad_rate_strategy(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateAdrateStrategyRequest, Mapping[str, Any]],
    ) -> None:
        """Change how a campaign sets its ad rates."""
        return await self._call(
            _update_ad_rate_strategy,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def update_bidding_strategy(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateBiddingStrategyRequest, Mapping[str, Any]],
    ) -> None:
        """Change the bidding strategy of a campaign."""
        return await self._call(
            _update_bidding_strategy,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def update_budget(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateCampaignBudgetRequest, Mapping[str, Any]],
    ) -> object:
        """Change the daily budget of a campaign."""
        return await self._call(
            _update_campaign_budget,
            campaign_id=campaign_id,
            _body=body,
        )

    @checked
    async def update_identification(
        self,
        campaign_id: StrictStr,
        body: Union[UpdateCampaignIdentificationRequest, Mapping[str, Any]],
    ) -> None:
        """Rename a campaign or change its dates."""
        return await self._call(
            _update_campaign_identification,
            campaign_id=campaign_id,
            _body=body,
        )
