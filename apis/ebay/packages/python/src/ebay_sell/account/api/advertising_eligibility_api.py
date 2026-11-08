# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.seller_eligibility_multi_program_response import SellerEligibilityMultiProgramResponse

_get_advertising_eligibility: Operation[SellerEligibilityMultiProgramResponse] = Operation(
    id="getAdvertisingEligibility",
    method="GET",
    path="/sell/account/v1/advertising_eligibility",
    resource="advertising_eligibility",
    name="get",
    params=(
        Param("program_types", "program_types", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=SellerEligibilityMultiProgramResponse,
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

OPERATIONS = (_get_advertising_eligibility,)


class AdvertisingEligibilityApi(Resource):
    @checked
    def get(
        self,
        *,
        program_types: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SellerEligibilityMultiProgramResponse:
        """Get the seller's eligibility for each advertising program."""
        return self._call(
            _get_advertising_eligibility,
            program_types=program_types,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncAdvertisingEligibilityApi(AsyncResource):
    @checked
    async def get(
        self,
        *,
        program_types: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SellerEligibilityMultiProgramResponse:
        """Get the seller's eligibility for each advertising program."""
        return await self._call(
            _get_advertising_eligibility,
            program_types=program_types,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
