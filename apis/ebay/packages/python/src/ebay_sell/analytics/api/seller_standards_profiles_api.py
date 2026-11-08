# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.analytics.models.find_seller_standards_profiles_response import FindSellerStandardsProfilesResponse
from ebay_sell.analytics.models.standards_profile import StandardsProfile

_find_seller_standards_profiles: Operation[FindSellerStandardsProfilesResponse] = Operation(
    id="findSellerStandardsProfiles",
    method="GET",
    path="/sell/analytics/v1/seller_standards_profile",
    resource="seller_standards_profiles",
    name="list",
    params=(),
    response=FindSellerStandardsProfilesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)
_get_seller_standards_profile: Operation[StandardsProfile] = Operation(
    id="getSellerStandardsProfile",
    method="GET",
    path="/sell/analytics/v1/seller_standards_profile/{program}/{cycle}",
    resource="seller_standards_profiles",
    name="get",
    params=(
        Param("cycle", "cycle", "path"),
        Param("program", "program", "path"),
    ),
    response=StandardsProfile,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)

OPERATIONS = (
    _find_seller_standards_profiles,
    _get_seller_standards_profile,
)


class SellerStandardsProfilesApi(Resource):
    @checked
    def list(
        self,
    ) -> FindSellerStandardsProfilesResponse:
        """List the seller's standards profiles."""
        return self._call(
            _find_seller_standards_profiles,
        )

    @checked
    def get(
        self,
        cycle: StrictStr,
        program: StrictStr,
    ) -> StandardsProfile:
        """Get one seller standards profile."""
        return self._call(
            _get_seller_standards_profile,
            cycle=cycle,
            program=program,
        )


class AsyncSellerStandardsProfilesApi(AsyncResource):
    @checked
    async def list(
        self,
    ) -> FindSellerStandardsProfilesResponse:
        """List the seller's standards profiles."""
        return await self._call(
            _find_seller_standards_profiles,
        )

    @checked
    async def get(
        self,
        cycle: StrictStr,
        program: StrictStr,
    ) -> StandardsProfile:
        """Get one seller standards profile."""
        return await self._call(
            _get_seller_standards_profile,
            cycle=cycle,
            program=program,
        )
