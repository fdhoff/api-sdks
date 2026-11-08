# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.return_policy import ReturnPolicy
from ebay_sell.account.models.return_policy_request import ReturnPolicyRequest
from ebay_sell.account.models.return_policy_response import ReturnPolicyResponse
from ebay_sell.account.models.set_return_policy_response import SetReturnPolicyResponse

_create_return_policy: Operation[SetReturnPolicyResponse] = Operation(
    id="createReturnPolicy",
    method="POST",
    path="/sell/account/v1/return_policy",
    resource="return_policies",
    name="create",
    params=(),
    response=SetReturnPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_delete_return_policy: Operation[None] = Operation(
    id="deleteReturnPolicy",
    method="DELETE",
    path="/sell/account/v1/return_policy/{return_policy_id}",
    resource="return_policies",
    name="delete",
    params=(Param("return_policy_id", "return_policy_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_get_return_policies: Operation[ReturnPolicyResponse] = Operation(
    id="getReturnPolicies",
    method="GET",
    path="/sell/account/v1/return_policy",
    resource="return_policies",
    name="list",
    params=(
        Param("marketplace_id", "marketplace_id", "query"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=ReturnPolicyResponse,
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
_get_return_policy: Operation[ReturnPolicy] = Operation(
    id="getReturnPolicy",
    method="GET",
    path="/sell/account/v1/return_policy/{return_policy_id}",
    resource="return_policies",
    name="get",
    params=(Param("return_policy_id", "return_policy_id", "path"),),
    response=ReturnPolicy,
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
_get_return_policy_by_name: Operation[ReturnPolicy] = Operation(
    id="getReturnPolicyByName",
    method="GET",
    path="/sell/account/v1/return_policy/get_by_policy_name",
    resource="return_policies",
    name="get_by_name",
    params=(
        Param("marketplace_id", "marketplace_id", "query"),
        Param("name", "name", "query"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=ReturnPolicy,
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
_update_return_policy: Operation[SetReturnPolicyResponse] = Operation(
    id="updateReturnPolicy",
    method="PUT",
    path="/sell/account/v1/return_policy/{return_policy_id}",
    resource="return_policies",
    name="update",
    params=(Param("return_policy_id", "return_policy_id", "path"),),
    response=SetReturnPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _create_return_policy,
    _delete_return_policy,
    _get_return_policies,
    _get_return_policy,
    _get_return_policy_by_name,
    _update_return_policy,
)


class ReturnPoliciesApi(Resource):
    @checked
    def create(
        self,
        body: Union[ReturnPolicyRequest, Mapping[str, Any]],
    ) -> SetReturnPolicyResponse:
        """Create a return policy."""
        return self._call(
            _create_return_policy,
            _body=body,
        )

    @checked
    def delete(
        self,
        return_policy_id: StrictStr,
    ) -> None:
        """Delete a return policy."""
        return self._call(
            _delete_return_policy,
            return_policy_id=return_policy_id,
        )

    @checked
    def list(
        self,
        *,
        marketplace_id: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> ReturnPolicyResponse:
        """List the seller's return policies on a marketplace."""
        return self._call(
            _get_return_policies,
            marketplace_id=marketplace_id,
            content_language=content_language,
        )

    @checked
    def get(
        self,
        return_policy_id: StrictStr,
    ) -> ReturnPolicy:
        """Get one return policy."""
        return self._call(
            _get_return_policy,
            return_policy_id=return_policy_id,
        )

    @checked
    def get_by_name(
        self,
        *,
        marketplace_id: StrictStr,
        name: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> ReturnPolicy:
        """Get a return policy by its name."""
        return self._call(
            _get_return_policy_by_name,
            marketplace_id=marketplace_id,
            name=name,
            content_language=content_language,
        )

    @checked
    def update(
        self,
        return_policy_id: StrictStr,
        body: Union[ReturnPolicyRequest, Mapping[str, Any]],
    ) -> SetReturnPolicyResponse:
        """Replace a return policy."""
        return self._call(
            _update_return_policy,
            return_policy_id=return_policy_id,
            _body=body,
        )


class AsyncReturnPoliciesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[ReturnPolicyRequest, Mapping[str, Any]],
    ) -> SetReturnPolicyResponse:
        """Create a return policy."""
        return await self._call(
            _create_return_policy,
            _body=body,
        )

    @checked
    async def delete(
        self,
        return_policy_id: StrictStr,
    ) -> None:
        """Delete a return policy."""
        return await self._call(
            _delete_return_policy,
            return_policy_id=return_policy_id,
        )

    @checked
    async def list(
        self,
        *,
        marketplace_id: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> ReturnPolicyResponse:
        """List the seller's return policies on a marketplace."""
        return await self._call(
            _get_return_policies,
            marketplace_id=marketplace_id,
            content_language=content_language,
        )

    @checked
    async def get(
        self,
        return_policy_id: StrictStr,
    ) -> ReturnPolicy:
        """Get one return policy."""
        return await self._call(
            _get_return_policy,
            return_policy_id=return_policy_id,
        )

    @checked
    async def get_by_name(
        self,
        *,
        marketplace_id: StrictStr,
        name: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> ReturnPolicy:
        """Get a return policy by its name."""
        return await self._call(
            _get_return_policy_by_name,
            marketplace_id=marketplace_id,
            name=name,
            content_language=content_language,
        )

    @checked
    async def update(
        self,
        return_policy_id: StrictStr,
        body: Union[ReturnPolicyRequest, Mapping[str, Any]],
    ) -> SetReturnPolicyResponse:
        """Replace a return policy."""
        return await self._call(
            _update_return_policy,
            return_policy_id=return_policy_id,
            _body=body,
        )
