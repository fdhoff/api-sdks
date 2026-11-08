# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.finances import models as _models
from ebay_sell.finances.models.payout import Payout
from ebay_sell.finances.models.payout_summary_response import PayoutSummaryResponse
from ebay_sell.finances.models.payouts import Payouts

_get_payout: Operation[Payout] = Operation(
    id="getPayout",
    method="GET",
    path="/sell/finances/v1/payout/{payout_Id}",
    resource="payouts",
    name="get",
    params=(
        Param("payout_Id", "payout_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=Payout,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)
_get_payout_summary: Operation[PayoutSummaryResponse] = Operation(
    id="getPayoutSummary",
    method="GET",
    path="/sell/finances/v1/payout_summary",
    resource="payouts",
    name="get_summary",
    params=(
        Param("filter", "filter", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=PayoutSummaryResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)
_get_payouts: Operation[Payouts] = Operation(
    id="getPayouts",
    method="GET",
    path="/sell/finances/v1/payout",
    resource="payouts",
    name="list",
    params=(
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=Payouts,
    returns_json=True,
    iterator="iter",
    item=_models.Payout,
    paging=NextLink(
        items="payouts",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)

OPERATIONS = (
    _get_payout,
    _get_payout_summary,
    _get_payouts,
)


class PayoutsApi(Resource):
    @checked
    def get(
        self,
        payout_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> Payout:
        """Get one payout."""
        return self._call(
            _get_payout,
            payout_id=payout_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
    ) -> PayoutSummaryResponse:
        """Sum the seller's payouts."""
        return self._call(
            _get_payout_summary,
            filter=filter,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def list(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Payouts:
        """List one page of the seller's payouts."""
        return self._call(
            _get_payouts,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.Payout]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_payouts,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncPayoutsApi(AsyncResource):
    @checked
    async def get(
        self,
        payout_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> Payout:
        """Get one payout."""
        return await self._call(
            _get_payout,
            payout_id=payout_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
    ) -> PayoutSummaryResponse:
        """Sum the seller's payouts."""
        return await self._call(
            _get_payout_summary,
            filter=filter,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def list(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Payouts:
        """List one page of the seller's payouts."""
        return await self._call(
            _get_payouts,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Payout]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_payouts,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
