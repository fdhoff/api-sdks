# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.analytics.models.report import Report

_get_traffic_report: Operation[Report] = Operation(
    id="getTrafficReport",
    method="GET",
    path="/sell/analytics/v1/traffic_report",
    resource="traffic_reports",
    name="get",
    params=(
        Param("dimension", "dimension", "query"),
        Param("filter", "filter", "query"),
        Param("metric", "metric", "query"),
        Param("sort", "sort", "query"),
    ),
    response=Report,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)

OPERATIONS = (_get_traffic_report,)


class TrafficReportsApi(Resource):
    @checked
    def get(
        self,
        *,
        dimension: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        metric: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Report:
        """Get a traffic report of the seller's listings."""
        return self._call(
            _get_traffic_report,
            dimension=dimension,
            filter=filter,
            metric=metric,
            sort=sort,
        )


class AsyncTrafficReportsApi(AsyncResource):
    @checked
    async def get(
        self,
        *,
        dimension: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        metric: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Report:
        """Get a traffic report of the seller's listings."""
        return await self._call(
            _get_traffic_report,
            dimension=dimension,
            filter=filter,
            metric=metric,
            sort=sort,
        )
