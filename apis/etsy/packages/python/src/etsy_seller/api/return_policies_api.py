# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import Field, StrictBool, StrictInt
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_return_policies import ShopReturnPolicies
from etsy_seller.models.shop_return_policy import ShopReturnPolicy

_consolidate_shop_return_policies: Operation[ShopReturnPolicy] = Operation(
    id="consolidateShopReturnPolicies",
    method="POST",
    path="/v3/application/shops/{shop_id}/policies/return/consolidate",
    resource="return_policies",
    name="consolidate",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("source_return_policy_id", "source_return_policy_id", "urlencoded"),
        Param("destination_return_policy_id", "destination_return_policy_id", "urlencoded"),
    ),
    response=ShopReturnPolicy,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_create_shop_return_policy: Operation[ShopReturnPolicy] = Operation(
    id="createShopReturnPolicy",
    method="POST",
    path="/v3/application/shops/{shop_id}/policies/return",
    resource="return_policies",
    name="create",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("accepts_returns", "accepts_returns", "urlencoded"),
        Param("accepts_exchanges", "accepts_exchanges", "urlencoded"),
        Param("return_deadline", "return_deadline", "urlencoded"),
    ),
    response=ShopReturnPolicy,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_delete_shop_return_policy: Operation[None] = Operation(
    id="deleteShopReturnPolicy",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/policies/return/{return_policy_id}",
    resource="return_policies",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("return_policy_id", "return_policy_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_get_shop_return_policies: Operation[ShopReturnPolicies] = Operation(
    id="getShopReturnPolicies",
    method="GET",
    path="/v3/application/shops/{shop_id}/policies/return",
    resource="return_policies",
    name="list",
    params=(Param("shop_id", "shop_id", "path"),),
    response=ShopReturnPolicies,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_shop_return_policy: Operation[ShopReturnPolicy] = Operation(
    id="getShopReturnPolicy",
    method="GET",
    path="/v3/application/shops/{shop_id}/policies/return/{return_policy_id}",
    resource="return_policies",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("return_policy_id", "return_policy_id", "path"),
    ),
    response=ShopReturnPolicy,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_shop_return_policy: Operation[ShopReturnPolicy] = Operation(
    id="updateShopReturnPolicy",
    method="PUT",
    path="/v3/application/shops/{shop_id}/policies/return/{return_policy_id}",
    resource="return_policies",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("return_policy_id", "return_policy_id", "path"),
        Param("accepts_returns", "accepts_returns", "urlencoded"),
        Param("accepts_exchanges", "accepts_exchanges", "urlencoded"),
        Param("return_deadline", "return_deadline", "urlencoded"),
    ),
    response=ShopReturnPolicy,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)

OPERATIONS = (
    _consolidate_shop_return_policies,
    _create_shop_return_policy,
    _delete_shop_return_policy,
    _get_shop_return_policies,
    _get_shop_return_policy,
    _update_shop_return_policy,
)


class ReturnPoliciesApi(Resource):
    @checked
    def consolidate(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        source_return_policy_id: Annotated[int, Field(strict=True, ge=1)],
        destination_return_policy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReturnPolicy:
        """Move every listing from one return policy to another and delete the first."""
        return self._call(
            _consolidate_shop_return_policies,
            shop_id=shop_id,
            source_return_policy_id=source_return_policy_id,
            destination_return_policy_id=destination_return_policy_id,
        )

    @checked
    def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        accepts_returns: StrictBool,
        accepts_exchanges: StrictBool,
        return_deadline: Optional[StrictInt] = None,
    ) -> ShopReturnPolicy:
        """Create a return policy."""
        return self._call(
            _create_shop_return_policy,
            shop_id=shop_id,
            accepts_returns=accepts_returns,
            accepts_exchanges=accepts_exchanges,
            return_deadline=return_deadline,
        )

    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a return policy."""
        return self._call(
            _delete_shop_return_policy,
            shop_id=shop_id,
            return_policy_id=return_policy_id,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReturnPolicies:
        """List a shop's return policies."""
        return self._call(
            _get_shop_return_policies,
            shop_id=shop_id,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReturnPolicy:
        """Get one return policy."""
        return self._call(
            _get_shop_return_policy,
            shop_id=shop_id,
            return_policy_id=return_policy_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        accepts_returns: StrictBool,
        accepts_exchanges: StrictBool,
        return_deadline: Optional[StrictInt] = None,
    ) -> ShopReturnPolicy:
        """Update a return policy."""
        return self._call(
            _update_shop_return_policy,
            shop_id=shop_id,
            return_policy_id=return_policy_id,
            accepts_returns=accepts_returns,
            accepts_exchanges=accepts_exchanges,
            return_deadline=return_deadline,
        )


class AsyncReturnPoliciesApi(AsyncResource):
    @checked
    async def consolidate(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        source_return_policy_id: Annotated[int, Field(strict=True, ge=1)],
        destination_return_policy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReturnPolicy:
        """Move every listing from one return policy to another and delete the first."""
        return await self._call(
            _consolidate_shop_return_policies,
            shop_id=shop_id,
            source_return_policy_id=source_return_policy_id,
            destination_return_policy_id=destination_return_policy_id,
        )

    @checked
    async def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        accepts_returns: StrictBool,
        accepts_exchanges: StrictBool,
        return_deadline: Optional[StrictInt] = None,
    ) -> ShopReturnPolicy:
        """Create a return policy."""
        return await self._call(
            _create_shop_return_policy,
            shop_id=shop_id,
            accepts_returns=accepts_returns,
            accepts_exchanges=accepts_exchanges,
            return_deadline=return_deadline,
        )

    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a return policy."""
        return await self._call(
            _delete_shop_return_policy,
            shop_id=shop_id,
            return_policy_id=return_policy_id,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReturnPolicies:
        """List a shop's return policies."""
        return await self._call(
            _get_shop_return_policies,
            shop_id=shop_id,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReturnPolicy:
        """Get one return policy."""
        return await self._call(
            _get_shop_return_policy,
            shop_id=shop_id,
            return_policy_id=return_policy_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        return_policy_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        accepts_returns: StrictBool,
        accepts_exchanges: StrictBool,
        return_deadline: Optional[StrictInt] = None,
    ) -> ShopReturnPolicy:
        """Update a return policy."""
        return await self._call(
            _update_shop_return_policy,
            shop_id=shop_id,
            return_policy_id=return_policy_id,
            accepts_returns=accepts_returns,
            accepts_exchanges=accepts_exchanges,
            return_deadline=return_deadline,
        )
