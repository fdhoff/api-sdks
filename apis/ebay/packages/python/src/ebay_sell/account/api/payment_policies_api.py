# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.payment_policy import PaymentPolicy
from ebay_sell.account.models.payment_policy_request import PaymentPolicyRequest
from ebay_sell.account.models.payment_policy_response import PaymentPolicyResponse
from ebay_sell.account.models.set_payment_policy_response import SetPaymentPolicyResponse

_create_payment_policy: Operation[SetPaymentPolicyResponse] = Operation(
    id="createPaymentPolicy",
    method="POST",
    path="/sell/account/v1/payment_policy",
    resource="payment_policies",
    name="create",
    params=(),
    response=SetPaymentPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_delete_payment_policy: Operation[None] = Operation(
    id="deletePaymentPolicy",
    method="DELETE",
    path="/sell/account/v1/payment_policy/{payment_policy_id}",
    resource="payment_policies",
    name="delete",
    params=(Param("payment_policy_id", "payment_policy_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_get_payment_policies: Operation[PaymentPolicyResponse] = Operation(
    id="getPaymentPolicies",
    method="GET",
    path="/sell/account/v1/payment_policy",
    resource="payment_policies",
    name="list",
    params=(
        Param("marketplace_id", "marketplace_id", "query"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=PaymentPolicyResponse,
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
_get_payment_policy: Operation[PaymentPolicy] = Operation(
    id="getPaymentPolicy",
    method="GET",
    path="/sell/account/v1/payment_policy/{payment_policy_id}",
    resource="payment_policies",
    name="get",
    params=(Param("payment_policy_id", "payment_policy_id", "path"),),
    response=PaymentPolicy,
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
_get_payment_policy_by_name: Operation[PaymentPolicy] = Operation(
    id="getPaymentPolicyByName",
    method="GET",
    path="/sell/account/v1/payment_policy/get_by_policy_name",
    resource="payment_policies",
    name="get_by_name",
    params=(
        Param("marketplace_id", "marketplace_id", "query"),
        Param("name", "name", "query"),
        Param("Content-Language", "content_language", "header"),
    ),
    response=PaymentPolicy,
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
_update_payment_policy: Operation[SetPaymentPolicyResponse] = Operation(
    id="updatePaymentPolicy",
    method="PUT",
    path="/sell/account/v1/payment_policy/{payment_policy_id}",
    resource="payment_policies",
    name="update",
    params=(Param("payment_policy_id", "payment_policy_id", "path"),),
    response=SetPaymentPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _create_payment_policy,
    _delete_payment_policy,
    _get_payment_policies,
    _get_payment_policy,
    _get_payment_policy_by_name,
    _update_payment_policy,
)


class PaymentPoliciesApi(Resource):
    @checked
    def create(
        self,
        body: Union[PaymentPolicyRequest, Mapping[str, Any]],
    ) -> SetPaymentPolicyResponse:
        """Create a payment policy."""
        return self._call(
            _create_payment_policy,
            _body=body,
        )

    @checked
    def delete(
        self,
        payment_policy_id: StrictStr,
    ) -> None:
        """Delete a payment policy."""
        return self._call(
            _delete_payment_policy,
            payment_policy_id=payment_policy_id,
        )

    @checked
    def list(
        self,
        *,
        marketplace_id: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> PaymentPolicyResponse:
        """List the seller's payment policies on a marketplace."""
        return self._call(
            _get_payment_policies,
            marketplace_id=marketplace_id,
            content_language=content_language,
        )

    @checked
    def get(
        self,
        payment_policy_id: StrictStr,
    ) -> PaymentPolicy:
        """Get one payment policy."""
        return self._call(
            _get_payment_policy,
            payment_policy_id=payment_policy_id,
        )

    @checked
    def get_by_name(
        self,
        *,
        marketplace_id: StrictStr,
        name: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> PaymentPolicy:
        """Get a payment policy by its name."""
        return self._call(
            _get_payment_policy_by_name,
            marketplace_id=marketplace_id,
            name=name,
            content_language=content_language,
        )

    @checked
    def update(
        self,
        payment_policy_id: StrictStr,
        body: Union[PaymentPolicyRequest, Mapping[str, Any]],
    ) -> SetPaymentPolicyResponse:
        """Replace a payment policy."""
        return self._call(
            _update_payment_policy,
            payment_policy_id=payment_policy_id,
            _body=body,
        )


class AsyncPaymentPoliciesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[PaymentPolicyRequest, Mapping[str, Any]],
    ) -> SetPaymentPolicyResponse:
        """Create a payment policy."""
        return await self._call(
            _create_payment_policy,
            _body=body,
        )

    @checked
    async def delete(
        self,
        payment_policy_id: StrictStr,
    ) -> None:
        """Delete a payment policy."""
        return await self._call(
            _delete_payment_policy,
            payment_policy_id=payment_policy_id,
        )

    @checked
    async def list(
        self,
        *,
        marketplace_id: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> PaymentPolicyResponse:
        """List the seller's payment policies on a marketplace."""
        return await self._call(
            _get_payment_policies,
            marketplace_id=marketplace_id,
            content_language=content_language,
        )

    @checked
    async def get(
        self,
        payment_policy_id: StrictStr,
    ) -> PaymentPolicy:
        """Get one payment policy."""
        return await self._call(
            _get_payment_policy,
            payment_policy_id=payment_policy_id,
        )

    @checked
    async def get_by_name(
        self,
        *,
        marketplace_id: StrictStr,
        name: StrictStr,
        content_language: Optional[StrictStr] = None,
    ) -> PaymentPolicy:
        """Get a payment policy by its name."""
        return await self._call(
            _get_payment_policy_by_name,
            marketplace_id=marketplace_id,
            name=name,
            content_language=content_language,
        )

    @checked
    async def update(
        self,
        payment_policy_id: StrictStr,
        body: Union[PaymentPolicyRequest, Mapping[str, Any]],
    ) -> SetPaymentPolicyResponse:
        """Replace a payment policy."""
        return await self._call(
            _update_payment_policy,
            payment_policy_id=payment_policy_id,
            _body=body,
        )
