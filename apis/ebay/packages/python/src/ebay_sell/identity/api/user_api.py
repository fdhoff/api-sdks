# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from ebay_sell._runtime import AsyncResource, Operation, Resource, Scheme, checked
from ebay_sell.identity.models.user_response import UserResponse

_get_user: Operation[UserResponse] = Operation(
    id="getUser",
    method="GET",
    path="/commerce/identity/v1/user/",
    resource="user",
    name="get",
    params=(),
    response=UserResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.identity.name.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.identity.address.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.identity.email.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.identity.phone.readonly",
                ),
            ),
        ),
    ),
    host="apiz",
)

OPERATIONS = (_get_user,)


class UserApi(Resource):
    @checked
    def get(
        self,
    ) -> UserResponse:
        """Get the account details of the user the token belongs to."""
        return self._call(
            _get_user,
        )


class AsyncUserApi(AsyncResource):
    @checked
    async def get(
        self,
    ) -> UserResponse:
        """Get the account details of the user the token belongs to."""
        return await self._call(
            _get_user,
        )
