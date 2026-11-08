# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from ebay_sell._runtime import AsyncResource, Operation, Resource, Scheme, checked
from ebay_sell.account_v2.models.payout_settings_response import PayoutSettingsResponse
from ebay_sell.account_v2.models.update_payout_percentage_request import UpdatePayoutPercentageRequest

_get_payout_settings: Operation[PayoutSettingsResponse] = Operation(
    id="getPayoutSettings",
    method="GET",
    path="/sell/account/v2/payout_settings",
    resource="payout_settings",
    name="get",
    params=(),
    response=PayoutSettingsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="api",
)
_update_payout_percentage: Operation[None] = Operation(
    id="updatePayoutPercentage",
    method="POST",
    path="/sell/account/v2/payout_settings/update_percentage",
    resource="payout_settings",
    name="update_percentage",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="api",
)

OPERATIONS = (
    _get_payout_settings,
    _update_payout_percentage,
)


class PayoutSettingsApi(Resource):
    @checked
    def get(
        self,
    ) -> PayoutSettingsResponse:
        """Get the seller's payout settings."""
        return self._call(
            _get_payout_settings,
        )

    @checked
    def update_percentage(
        self,
        body: Optional[Union[UpdatePayoutPercentageRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Split payouts between the seller's payout accounts."""
        return self._call(
            _update_payout_percentage,
            _body=body,
        )


class AsyncPayoutSettingsApi(AsyncResource):
    @checked
    async def get(
        self,
    ) -> PayoutSettingsResponse:
        """Get the seller's payout settings."""
        return await self._call(
            _get_payout_settings,
        )

    @checked
    async def update_percentage(
        self,
        body: Optional[Union[UpdatePayoutPercentageRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Split payouts between the seller's payout accounts."""
        return await self._call(
            _update_payout_percentage,
            _body=body,
        )
