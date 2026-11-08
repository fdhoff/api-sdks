# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.user_address import UserAddress
from etsy_seller.models.user_addresses import UserAddresses

_get_user_address: Operation[UserAddress] = Operation(
    id="getUserAddress",
    method="GET",
    path="/v3/application/user/addresses/{user_address_id}",
    resource="user_addresses",
    name="get",
    params=(Param("user_address_id", "user_address_id", "path"),),
    response=UserAddress,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("address_r",)),
        ),
    ),
)
_get_user_addresses: Operation[UserAddresses] = Operation(
    id="getUserAddresses",
    method="GET",
    path="/v3/application/user/addresses",
    resource="user_addresses",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=UserAddresses,
    returns_json=True,
    iterator="iter",
    item=_models.UserAddress,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("address_r",)),
        ),
    ),
)

OPERATIONS = (
    _get_user_address,
    _get_user_addresses,
)


class UserAddressesApi(Resource):
    @checked
    def get(
        self,
        user_address_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> UserAddress:
        """Get one of the user&#39;s addresses."""
        return self._call(
            _get_user_address,
            user_address_id=user_address_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> UserAddresses:
        """List one page of the user&#39;s addresses."""
        return self._call(
            _get_user_addresses,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.UserAddress]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_addresses,
            limit=limit,
            offset=offset,
        )


class AsyncUserAddressesApi(AsyncResource):
    @checked
    async def get(
        self,
        user_address_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> UserAddress:
        """Get one of the user&#39;s addresses."""
        return await self._call(
            _get_user_address,
            user_address_id=user_address_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> UserAddresses:
        """List one page of the user&#39;s addresses."""
        return await self._call(
            _get_user_addresses,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.UserAddress]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_user_addresses,
            limit=limit,
            offset=offset,
        )
