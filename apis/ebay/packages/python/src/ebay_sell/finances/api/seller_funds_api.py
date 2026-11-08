# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.finances.models.seller_funds_summary_response import SellerFundsSummaryResponse

_get_seller_funds_summary: Operation[SellerFundsSummaryResponse] = Operation(
    id="getSellerFundsSummary",
    method="GET",
    path="/sell/finances/v1/seller_funds_summary",
    resource="seller_funds",
    name="get_summary",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=SellerFundsSummaryResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)

OPERATIONS = (_get_seller_funds_summary,)


class SellerFundsApi(Resource):
    @checked
    def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SellerFundsSummaryResponse:
        """Get the seller's funds that are not yet paid out."""
        return self._call(
            _get_seller_funds_summary,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncSellerFundsApi(AsyncResource):
    @checked
    async def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SellerFundsSummaryResponse:
        """Get the seller's funds that are not yet paid out."""
        return await self._call(
            _get_seller_funds_summary,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
