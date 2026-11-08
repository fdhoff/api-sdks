# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.finances import models as _models
from ebay_sell.finances.models.billing_activity_response import BillingActivityResponse

_get_billing_activities: Operation[BillingActivityResponse] = Operation(
    id="getBillingActivities",
    method="GET",
    path="/sell/finances/v1/billing_activity",
    resource="billing_activities",
    name="list",
    params=(
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
    ),
    response=BillingActivityResponse,
    returns_json=True,
    iterator="iter",
    item=_models.BillingActivityLineItem,
    paging=NextLink(
        items="billingActivities",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="api",
)

OPERATIONS = (_get_billing_activities,)


class BillingActivitiesApi(Resource):
    @checked
    def list(
        self,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> BillingActivityResponse:
        """List one page of the seller's billing activities."""
        return self._call(
            _get_billing_activities,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.BillingActivityLineItem]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_billing_activities,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
        )


class AsyncBillingActivitiesApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> BillingActivityResponse:
        """List one page of the seller's billing activities."""
        return await self._call(
            _get_billing_activities,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.BillingActivityLineItem]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_billing_activities,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
        )
