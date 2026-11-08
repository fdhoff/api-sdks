# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from ebay_sell._runtime import AsyncResource, Operation, Resource, Scheme, checked
from ebay_sell.account.models.selling_privileges import SellingPrivileges

_get_privileges: Operation[SellingPrivileges] = Operation(
    id="getPrivileges",
    method="GET",
    path="/sell/account/v1/privilege",
    resource="privileges",
    name="get",
    params=(),
    response=SellingPrivileges,
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

OPERATIONS = (_get_privileges,)


class PrivilegesApi(Resource):
    @checked
    def get(
        self,
    ) -> SellingPrivileges:
        """Get the seller's selling limits and registration status."""
        return self._call(
            _get_privileges,
        )


class AsyncPrivilegesApi(AsyncResource):
    @checked
    async def get(
        self,
    ) -> SellingPrivileges:
        """Get the seller's selling limits and registration status."""
        return await self._call(
            _get_privileges,
        )
