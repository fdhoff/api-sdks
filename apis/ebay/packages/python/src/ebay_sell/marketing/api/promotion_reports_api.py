# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.promotions_report_paged_collection import PromotionsReportPagedCollection
from ebay_sell.marketing.models.summary_report_response import SummaryReportResponse

_get_promotion_reports: Operation[PromotionsReportPagedCollection] = Operation(
    id="getPromotionReports",
    method="GET",
    path="/sell/marketing/v1/promotion_report",
    resource="promotion_reports",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("marketplace_id", "marketplace_id", "query"),
        Param("offset", "offset", "query"),
        Param("promotion_status", "promotion_status", "query"),
        Param("promotion_type", "promotion_type", "query"),
        Param("q", "q", "query"),
    ),
    response=PromotionsReportPagedCollection,
    returns_json=True,
    iterator="iter",
    item=_models.PromotionReportDetail,
    paging=NextLink(
        items="promotionReports",
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
_get_promotion_summary_report: Operation[SummaryReportResponse] = Operation(
    id="getPromotionSummaryReport",
    method="GET",
    path="/sell/marketing/v1/promotion_summary_report",
    resource="promotion_reports",
    name="get_summary",
    params=(Param("marketplace_id", "marketplace_id", "query"),),
    response=SummaryReportResponse,
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

OPERATIONS = (
    _get_promotion_reports,
    _get_promotion_summary_report,
)


class PromotionReportsApi(Resource):
    @checked
    def list(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> PromotionsReportPagedCollection:
        """List one page of promotion performance reports."""
        return self._call(
            _get_promotion_reports,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
        )

    @checked
    def iter(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> Iterator[_models.PromotionReportDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_promotion_reports,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
        )

    @checked
    def get_summary(
        self,
        *,
        marketplace_id: StrictStr,
    ) -> SummaryReportResponse:
        """Get a summary of the seller's promotion performance."""
        return self._call(
            _get_promotion_summary_report,
            marketplace_id=marketplace_id,
        )


class AsyncPromotionReportsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> PromotionsReportPagedCollection:
        """List one page of promotion performance reports."""
        return await self._call(
            _get_promotion_reports,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
        )

    @checked
    def iter(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.PromotionReportDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_promotion_reports,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
        )

    @checked
    async def get_summary(
        self,
        *,
        marketplace_id: StrictStr,
    ) -> SummaryReportResponse:
        """Get a summary of the seller's promotion performance."""
        return await self._call(
            _get_promotion_summary_report,
            marketplace_id=marketplace_id,
        )
