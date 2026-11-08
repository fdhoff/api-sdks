# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account_v2.models.rate_table_details import RateTableDetails
from ebay_sell.account_v2.models.rate_table_update import RateTableUpdate

_get_rate_table: Operation[RateTableDetails] = Operation(
    id="getRateTable",
    method="GET",
    path="/sell/account/v2/rate_table/{rate_table_id}",
    resource="rate_tables",
    name="get",
    params=(Param("rate_table_id", "rate_table_id", "path"),),
    response=RateTableDetails,
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
_update_shipping_cost: Operation[None] = Operation(
    id="updateShippingCost",
    method="POST",
    path="/sell/account/v2/rate_table/{rate_table_id}/update_shipping_cost",
    resource="rate_tables",
    name="update_shipping_cost",
    params=(Param("rate_table_id", "rate_table_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _get_rate_table,
    _update_shipping_cost,
)


class RateTablesApi(Resource):
    @checked
    def get(
        self,
        rate_table_id: StrictStr,
    ) -> RateTableDetails:
        """Get one shipping rate table."""
        return self._call(
            _get_rate_table,
            rate_table_id=rate_table_id,
        )

    @checked
    def update_shipping_cost(
        self,
        rate_table_id: StrictStr,
        body: Optional[Union[RateTableUpdate, Mapping[str, Any]]] = None,
    ) -> None:
        """Update the shipping costs in a rate table."""
        return self._call(
            _update_shipping_cost,
            rate_table_id=rate_table_id,
            _body=body,
        )


class AsyncRateTablesApi(AsyncResource):
    @checked
    async def get(
        self,
        rate_table_id: StrictStr,
    ) -> RateTableDetails:
        """Get one shipping rate table."""
        return await self._call(
            _get_rate_table,
            rate_table_id=rate_table_id,
        )

    @checked
    async def update_shipping_cost(
        self,
        rate_table_id: StrictStr,
        body: Optional[Union[RateTableUpdate, Mapping[str, Any]]] = None,
    ) -> None:
        """Update the shipping costs in a rate table."""
        return await self._call(
            _update_shipping_cost,
            rate_table_id=rate_table_id,
            _body=body,
        )
