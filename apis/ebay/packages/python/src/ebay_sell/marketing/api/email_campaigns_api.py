# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.create_email_campaign_request import CreateEmailCampaignRequest
from ebay_sell.marketing.models.create_email_campaign_response import CreateEmailCampaignResponse
from ebay_sell.marketing.models.delete_email_campaign_response import DeleteEmailCampaignResponse
from ebay_sell.marketing.models.get_email_campaign_audiences_response import GetEmailCampaignAudiencesResponse
from ebay_sell.marketing.models.get_email_campaign_response import GetEmailCampaignResponse
from ebay_sell.marketing.models.get_email_campaigns_response import GetEmailCampaignsResponse
from ebay_sell.marketing.models.get_email_preview_response import GetEmailPreviewResponse
from ebay_sell.marketing.models.get_email_report_response import GetEmailReportResponse
from ebay_sell.marketing.models.update_campaign_request import UpdateCampaignRequest
from ebay_sell.marketing.models.update_email_campaign_response import UpdateEmailCampaignResponse

_create_email_campaign: Operation[CreateEmailCampaignResponse] = Operation(
    id="createEmailCampaign",
    method="POST",
    path="/sell/marketing/v1/email_campaign",
    resource="email_campaigns",
    name="create",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=CreateEmailCampaignResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_email_campaign: Operation[DeleteEmailCampaignResponse] = Operation(
    id="deleteEmailCampaign",
    method="DELETE",
    path="/sell/marketing/v1/email_campaign/{email_campaign_id}",
    resource="email_campaigns",
    name="delete",
    params=(Param("email_campaign_id", "email_campaign_id", "path"),),
    response=DeleteEmailCampaignResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_audiences: Operation[GetEmailCampaignAudiencesResponse] = Operation(
    id="getAudiences",
    method="GET",
    path="/sell/marketing/v1/email_campaign/audience",
    resource="email_campaigns",
    name="list_audiences",
    params=(
        Param("emailCampaignType", "email_campaign_type", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=GetEmailCampaignAudiencesResponse,
    returns_json=True,
    iterator="iter_audiences",
    item=_models.CampaignAudience,
    paging=NextLink(
        items="audiences",
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
_get_email_campaign: Operation[GetEmailCampaignResponse] = Operation(
    id="getEmailCampaign",
    method="GET",
    path="/sell/marketing/v1/email_campaign/{email_campaign_id}",
    resource="email_campaigns",
    name="get",
    params=(Param("email_campaign_id", "email_campaign_id", "path"),),
    response=GetEmailCampaignResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_email_campaigns: Operation[GetEmailCampaignsResponse] = Operation(
    id="getEmailCampaigns",
    method="GET",
    path="/sell/marketing/v1/email_campaign",
    resource="email_campaigns",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("q", "q", "query"),
        Param("sort", "sort", "query"),
    ),
    response=GetEmailCampaignsResponse,
    returns_json=True,
    iterator="iter",
    item=_models.CampaignDTO,
    paging=NextLink(
        items="campaigns",
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
_get_email_preview: Operation[GetEmailPreviewResponse] = Operation(
    id="getEmailPreview",
    method="GET",
    path="/sell/marketing/v1/email_campaign/{email_campaign_id}/email_preview",
    resource="email_campaigns",
    name="get_preview",
    params=(Param("email_campaign_id", "email_campaign_id", "path"),),
    response=GetEmailPreviewResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_email_report: Operation[GetEmailReportResponse] = Operation(
    id="getEmailReport",
    method="GET",
    path="/sell/marketing/v1/email_campaign/report",
    resource="email_campaigns",
    name="get_report",
    params=(
        Param("endDate", "end_date", "query"),
        Param("startDate", "start_date", "query"),
    ),
    response=GetEmailReportResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_email_campaign: Operation[UpdateEmailCampaignResponse] = Operation(
    id="updateEmailCampaign",
    method="PUT",
    path="/sell/marketing/v1/email_campaign/{email_campaign_id}",
    resource="email_campaigns",
    name="update",
    params=(Param("email_campaign_id", "email_campaign_id", "path"),),
    response=UpdateEmailCampaignResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _create_email_campaign,
    _delete_email_campaign,
    _get_audiences,
    _get_email_campaign,
    _get_email_campaigns,
    _get_email_preview,
    _get_email_report,
    _update_email_campaign,
)


class EmailCampaignsApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateEmailCampaignRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> CreateEmailCampaignResponse:
        """Create a store email campaign."""
        return self._call(
            _create_email_campaign,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def delete(
        self,
        email_campaign_id: StrictStr,
    ) -> DeleteEmailCampaignResponse:
        """Delete an email campaign."""
        return self._call(
            _delete_email_campaign,
            email_campaign_id=email_campaign_id,
        )

    @checked
    def list_audiences(
        self,
        *,
        email_campaign_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> GetEmailCampaignAudiencesResponse:
        """List one page of the audiences an email campaign can target."""
        return self._call(
            _get_audiences,
            email_campaign_type=email_campaign_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_audiences(
        self,
        *,
        email_campaign_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.CampaignAudience]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_audiences,
            email_campaign_type=email_campaign_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def get(
        self,
        email_campaign_id: StrictStr,
    ) -> GetEmailCampaignResponse:
        """Get one email campaign."""
        return self._call(
            _get_email_campaign,
            email_campaign_id=email_campaign_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> GetEmailCampaignsResponse:
        """List one page of the seller's store email campaigns."""
        return self._call(
            _get_email_campaigns,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.CampaignDTO]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_email_campaigns,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
        )

    @checked
    def get_preview(
        self,
        email_campaign_id: StrictStr,
    ) -> GetEmailPreviewResponse:
        """Preview the email of a campaign."""
        return self._call(
            _get_email_preview,
            email_campaign_id=email_campaign_id,
        )

    @checked
    def get_report(
        self,
        *,
        end_date: StrictStr,
        start_date: StrictStr,
    ) -> GetEmailReportResponse:
        """Get the performance of the seller's email campaigns."""
        return self._call(
            _get_email_report,
            end_date=end_date,
            start_date=start_date,
        )

    @checked
    def update(
        self,
        email_campaign_id: StrictStr,
        body: Union[UpdateCampaignRequest, Mapping[str, Any]],
    ) -> UpdateEmailCampaignResponse:
        """Update an email campaign."""
        return self._call(
            _update_email_campaign,
            email_campaign_id=email_campaign_id,
            _body=body,
        )


class AsyncEmailCampaignsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateEmailCampaignRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> CreateEmailCampaignResponse:
        """Create a store email campaign."""
        return await self._call(
            _create_email_campaign,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def delete(
        self,
        email_campaign_id: StrictStr,
    ) -> DeleteEmailCampaignResponse:
        """Delete an email campaign."""
        return await self._call(
            _delete_email_campaign,
            email_campaign_id=email_campaign_id,
        )

    @checked
    async def list_audiences(
        self,
        *,
        email_campaign_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> GetEmailCampaignAudiencesResponse:
        """List one page of the audiences an email campaign can target."""
        return await self._call(
            _get_audiences,
            email_campaign_type=email_campaign_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_audiences(
        self,
        *,
        email_campaign_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.CampaignAudience]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_audiences,
            email_campaign_type=email_campaign_type,
            limit=limit,
            offset=offset,
        )

    @checked
    async def get(
        self,
        email_campaign_id: StrictStr,
    ) -> GetEmailCampaignResponse:
        """Get one email campaign."""
        return await self._call(
            _get_email_campaign,
            email_campaign_id=email_campaign_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> GetEmailCampaignsResponse:
        """List one page of the seller's store email campaigns."""
        return await self._call(
            _get_email_campaigns,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.CampaignDTO]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_email_campaigns,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
        )

    @checked
    async def get_preview(
        self,
        email_campaign_id: StrictStr,
    ) -> GetEmailPreviewResponse:
        """Preview the email of a campaign."""
        return await self._call(
            _get_email_preview,
            email_campaign_id=email_campaign_id,
        )

    @checked
    async def get_report(
        self,
        *,
        end_date: StrictStr,
        start_date: StrictStr,
    ) -> GetEmailReportResponse:
        """Get the performance of the seller's email campaigns."""
        return await self._call(
            _get_email_report,
            end_date=end_date,
            start_date=start_date,
        )

    @checked
    async def update(
        self,
        email_campaign_id: StrictStr,
        body: Union[UpdateCampaignRequest, Mapping[str, Any]],
    ) -> UpdateEmailCampaignResponse:
        """Update an email campaign."""
        return await self._call(
            _update_email_campaign,
            email_campaign_id=email_campaign_id,
            _body=body,
        )
