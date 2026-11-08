# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.fulfillment_policy import FulfillmentPolicy
from ebay_sell.account.models.fulfillment_policy_request import FulfillmentPolicyRequest
from ebay_sell.account.models.fulfillment_policy_response import FulfillmentPolicyResponse
from ebay_sell.account.models.set_fulfillment_policy_response import SetFulfillmentPolicyResponse

_create_fulfillment_policy: Operation[SetFulfillmentPolicyResponse] = Operation(
    id="createFulfillmentPolicy",
    method="POST",
    path="/sell/account/v1/fulfillment_policy/",
    resource="fulfillment_policies",
    name="create",
    params=(),
    response=SetFulfillmentPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_delete_fulfillment_policy: Operation[None] = Operation(
    id="deleteFulfillmentPolicy",
    method="DELETE",
    path="/sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}",
    resource="fulfillment_policies",
    name="delete",
    params=(Param("fulfillmentPolicyId", "fulfillment_policy_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_get_fulfillment_policies: Operation[FulfillmentPolicyResponse] = Operation(
    id="getFulfillmentPolicies",
    method="GET",
    path="/sell/account/v1/fulfillment_policy",
    resource="fulfillment_policies",
    name="list",
    params=(
        Param("marketplace_id", "marketplace_id", "query"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=FulfillmentPolicyResponse,
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
_get_fulfillment_policy: Operation[FulfillmentPolicy] = Operation(
    id="getFulfillmentPolicy",
    method="GET",
    path="/sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}",
    resource="fulfillment_policies",
    name="get",
    params=(Param("fulfillmentPolicyId", "fulfillment_policy_id", "path"),),
    response=FulfillmentPolicy,
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
_get_fulfillment_policy_by_name: Operation[FulfillmentPolicy] = Operation(
    id="getFulfillmentPolicyByName",
    method="GET",
    path="/sell/account/v1/fulfillment_policy/get_by_policy_name",
    resource="fulfillment_policies",
    name="get_by_name",
    params=(
        Param("marketplace_id", "marketplace_id", "query"),
        Param("name", "name", "query"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=FulfillmentPolicy,
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
_update_fulfillment_policy: Operation[SetFulfillmentPolicyResponse] = Operation(
    id="updateFulfillmentPolicy",
    method="PUT",
    path="/sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}",
    resource="fulfillment_policies",
    name="update",
    params=(Param("fulfillmentPolicyId", "fulfillment_policy_id", "path"),),
    response=SetFulfillmentPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _create_fulfillment_policy,
    _delete_fulfillment_policy,
    _get_fulfillment_policies,
    _get_fulfillment_policy,
    _get_fulfillment_policy_by_name,
    _update_fulfillment_policy,
)


class FulfillmentPoliciesApi(Resource):
    @checked
    def create(
        self,
        body: Union[FulfillmentPolicyRequest, Mapping[str, Any]],
    ) -> SetFulfillmentPolicyResponse:
        """Create a fulfillment policy."""
        return self._call(
            _create_fulfillment_policy,
            _body=body,
        )

    @checked
    def delete(
        self,
        fulfillment_policy_id: StrictStr,
    ) -> None:
        """Delete a fulfillment policy."""
        return self._call(
            _delete_fulfillment_policy,
            fulfillment_policy_id=fulfillment_policy_id,
        )

    @checked
    def list(
        self,
        *,
        marketplace_id: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> FulfillmentPolicyResponse:
        """List the seller's fulfillment policies on a marketplace."""
        return self._call(
            _get_fulfillment_policies,
            marketplace_id=marketplace_id,
            content_language=content_language,
        )

    @checked
    def get(
        self,
        fulfillment_policy_id: StrictStr,
    ) -> FulfillmentPolicy:
        """Get one fulfillment policy."""
        return self._call(
            _get_fulfillment_policy,
            fulfillment_policy_id=fulfillment_policy_id,
        )

    @checked
    def get_by_name(
        self,
        *,
        marketplace_id: StrictStr,
        name: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> FulfillmentPolicy:
        """Get a fulfillment policy by its name."""
        return self._call(
            _get_fulfillment_policy_by_name,
            marketplace_id=marketplace_id,
            name=name,
            content_language=content_language,
        )

    @checked
    def update(
        self,
        fulfillment_policy_id: StrictStr,
        body: Union[FulfillmentPolicyRequest, Mapping[str, Any]],
    ) -> SetFulfillmentPolicyResponse:
        """Replace a fulfillment policy."""
        return self._call(
            _update_fulfillment_policy,
            fulfillment_policy_id=fulfillment_policy_id,
            _body=body,
        )


class AsyncFulfillmentPoliciesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[FulfillmentPolicyRequest, Mapping[str, Any]],
    ) -> SetFulfillmentPolicyResponse:
        """Create a fulfillment policy."""
        return await self._call(
            _create_fulfillment_policy,
            _body=body,
        )

    @checked
    async def delete(
        self,
        fulfillment_policy_id: StrictStr,
    ) -> None:
        """Delete a fulfillment policy."""
        return await self._call(
            _delete_fulfillment_policy,
            fulfillment_policy_id=fulfillment_policy_id,
        )

    @checked
    async def list(
        self,
        *,
        marketplace_id: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> FulfillmentPolicyResponse:
        """List the seller's fulfillment policies on a marketplace."""
        return await self._call(
            _get_fulfillment_policies,
            marketplace_id=marketplace_id,
            content_language=content_language,
        )

    @checked
    async def get(
        self,
        fulfillment_policy_id: StrictStr,
    ) -> FulfillmentPolicy:
        """Get one fulfillment policy."""
        return await self._call(
            _get_fulfillment_policy,
            fulfillment_policy_id=fulfillment_policy_id,
        )

    @checked
    async def get_by_name(
        self,
        *,
        marketplace_id: StrictStr,
        name: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> FulfillmentPolicy:
        """Get a fulfillment policy by its name."""
        return await self._call(
            _get_fulfillment_policy_by_name,
            marketplace_id=marketplace_id,
            name=name,
            content_language=content_language,
        )

    @checked
    async def update(
        self,
        fulfillment_policy_id: StrictStr,
        body: Union[FulfillmentPolicyRequest, Mapping[str, Any]],
    ) -> SetFulfillmentPolicyResponse:
        """Replace a fulfillment policy."""
        return await self._call(
            _update_fulfillment_policy,
            fulfillment_policy_id=fulfillment_policy_id,
            _body=body,
        )
