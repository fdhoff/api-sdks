# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from ebay_sell._runtime import AsyncResource, Operation, Resource, Scheme, checked
from ebay_sell.account.models.kyc_response import KycResponse

_get_kyc: Operation[KycResponse] = Operation(
    id="getKYC",
    method="GET",
    path="/sell/account/v1/kyc",
    resource="kyc",
    name="get",
    params=(),
    response=KycResponse,
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

OPERATIONS = (_get_kyc,)


class KycApi(Resource):
    @checked
    def get(
        self,
    ) -> KycResponse:
        """List the identity checks eBay needs from the seller."""
        return self._call(
            _get_kyc,
        )


class AsyncKycApi(AsyncResource):
    @checked
    async def get(
        self,
    ) -> KycResponse:
        """List the identity checks eBay needs from the seller."""
        return await self._call(
            _get_kyc,
        )
