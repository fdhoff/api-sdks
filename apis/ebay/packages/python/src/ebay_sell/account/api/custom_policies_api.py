# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.custom_policy import CustomPolicy
from ebay_sell.account.models.custom_policy_create_request import CustomPolicyCreateRequest
from ebay_sell.account.models.custom_policy_request import CustomPolicyRequest
from ebay_sell.account.models.custom_policy_response import CustomPolicyResponse

_create_custom_policy: Operation[object] = Operation(
    id="createCustomPolicy",
    method="POST",
    path="/sell/account/v1/custom_policy/",
    resource="custom_policies",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_get_custom_policies: Operation[CustomPolicyResponse] = Operation(
    id="getCustomPolicies",
    method="GET",
    path="/sell/account/v1/custom_policy/",
    resource="custom_policies",
    name="list",
    params=(Param("policy_types", "policy_types", "query"),),
    response=CustomPolicyResponse,
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
_get_custom_policy: Operation[CustomPolicy] = Operation(
    id="getCustomPolicy",
    method="GET",
    path="/sell/account/v1/custom_policy/{custom_policy_id}",
    resource="custom_policies",
    name="get",
    params=(Param("custom_policy_id", "custom_policy_id", "path"),),
    response=CustomPolicy,
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
_update_custom_policy: Operation[None] = Operation(
    id="updateCustomPolicy",
    method="PUT",
    path="/sell/account/v1/custom_policy/{custom_policy_id}",
    resource="custom_policies",
    name="update",
    params=(Param("custom_policy_id", "custom_policy_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _create_custom_policy,
    _get_custom_policies,
    _get_custom_policy,
    _update_custom_policy,
)


class CustomPoliciesApi(Resource):
    @checked
    def create(
        self,
        body: Union[CustomPolicyCreateRequest, Mapping[str, Any]],
    ) -> object:
        """Create a custom policy."""
        return self._call(
            _create_custom_policy,
            _body=body,
        )

    @checked
    def list(
        self,
        *,
        policy_types: Optional[StrictStr] = None,
    ) -> CustomPolicyResponse:
        """List the seller's custom policies."""
        return self._call(
            _get_custom_policies,
            policy_types=policy_types,
        )

    @checked
    def get(
        self,
        custom_policy_id: StrictStr,
    ) -> CustomPolicy:
        """Get one custom policy."""
        return self._call(
            _get_custom_policy,
            custom_policy_id=custom_policy_id,
        )

    @checked
    def update(
        self,
        custom_policy_id: StrictStr,
        body: Union[CustomPolicyRequest, Mapping[str, Any]],
    ) -> None:
        """Update a custom policy."""
        return self._call(
            _update_custom_policy,
            custom_policy_id=custom_policy_id,
            _body=body,
        )


class AsyncCustomPoliciesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CustomPolicyCreateRequest, Mapping[str, Any]],
    ) -> object:
        """Create a custom policy."""
        return await self._call(
            _create_custom_policy,
            _body=body,
        )

    @checked
    async def list(
        self,
        *,
        policy_types: Optional[StrictStr] = None,
    ) -> CustomPolicyResponse:
        """List the seller's custom policies."""
        return await self._call(
            _get_custom_policies,
            policy_types=policy_types,
        )

    @checked
    async def get(
        self,
        custom_policy_id: StrictStr,
    ) -> CustomPolicy:
        """Get one custom policy."""
        return await self._call(
            _get_custom_policy,
            custom_policy_id=custom_policy_id,
        )

    @checked
    async def update(
        self,
        custom_policy_id: StrictStr,
        body: Union[CustomPolicyRequest, Mapping[str, Any]],
    ) -> None:
        """Update a custom policy."""
        return await self._call(
            _update_custom_policy,
            custom_policy_id=custom_policy_id,
            _body=body,
        )
