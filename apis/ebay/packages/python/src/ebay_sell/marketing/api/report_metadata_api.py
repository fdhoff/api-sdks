# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing.models.report_metadata import ReportMetadata
from ebay_sell.marketing.models.report_metadatas import ReportMetadatas

_get_report_metadata: Operation[ReportMetadatas] = Operation(
    id="getReportMetadata",
    method="GET",
    path="/sell/marketing/v1/ad_report_metadata",
    resource="report_metadata",
    name="list",
    params=(
        Param("funding_model", "funding_model", "query"),
        Param("channel", "channel", "query"),
    ),
    response=ReportMetadatas,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_report_metadata_for_report_type: Operation[ReportMetadata] = Operation(
    id="getReportMetadataForReportType",
    method="GET",
    path="/sell/marketing/v1/ad_report_metadata/{report_type}",
    resource="report_metadata",
    name="get",
    params=(
        Param("report_type", "report_type", "path"),
        Param("funding_model", "funding_model", "query"),
        Param("channel", "channel", "query"),
    ),
    response=ReportMetadata,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _get_report_metadata,
    _get_report_metadata_for_report_type,
)


class ReportMetadataApi(Resource):
    @checked
    def list(
        self,
        *,
        funding_model: Optional[StrictStr] = None,
        channel: Optional[StrictStr] = None,
    ) -> ReportMetadatas:
        """List the fields of every Promoted Listings report type."""
        return self._call(
            _get_report_metadata,
            funding_model=funding_model,
            channel=channel,
        )

    @checked
    def get(
        self,
        report_type: StrictStr,
        *,
        funding_model: Optional[StrictStr] = None,
        channel: Optional[StrictStr] = None,
    ) -> ReportMetadata:
        """List the fields of one report type."""
        return self._call(
            _get_report_metadata_for_report_type,
            report_type=report_type,
            funding_model=funding_model,
            channel=channel,
        )


class AsyncReportMetadataApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        funding_model: Optional[StrictStr] = None,
        channel: Optional[StrictStr] = None,
    ) -> ReportMetadatas:
        """List the fields of every Promoted Listings report type."""
        return await self._call(
            _get_report_metadata,
            funding_model=funding_model,
            channel=channel,
        )

    @checked
    async def get(
        self,
        report_type: StrictStr,
        *,
        funding_model: Optional[StrictStr] = None,
        channel: Optional[StrictStr] = None,
    ) -> ReportMetadata:
        """List the fields of one report type."""
        return await self._call(
            _get_report_metadata_for_report_type,
            report_type=report_type,
            funding_model=funding_model,
            channel=channel,
        )
