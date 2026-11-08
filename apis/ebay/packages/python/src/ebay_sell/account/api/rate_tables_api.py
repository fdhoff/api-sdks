# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.rate_table_response import RateTableResponse

_get_rate_tables: Operation[RateTableResponse] = Operation(
    id="getRateTables",
    method="GET",
    path="/sell/account/v1/rate_table",
    resource="rate_tables",
    name="list",
    params=(Param("country_code", "country_code", "query"),),
    response=RateTableResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.account.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (_get_rate_tables,)


class RateTablesApi(Resource):
    @checked
    def list(
        self,
        *,
        country_code: Optional[StrictStr] = None,
    ) -> RateTableResponse:
        """List the seller's shipping rate tables."""
        return self._call(
            _get_rate_tables,
            country_code=country_code,
        )


class AsyncRateTablesApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        country_code: Optional[StrictStr] = None,
    ) -> RateTableResponse:
        """List the seller's shipping rate tables."""
        return await self._call(
            _get_rate_tables,
            country_code=country_code,
        )
