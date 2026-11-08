# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop import Shop
from etsy_seller.models.shops import Shops

_find_shops: Operation[Shops] = Operation(
    id="findShops",
    method="GET",
    path="/v3/application/shops",
    resource="shops",
    name="find",
    params=(
        Param("shop_name", "shop_name", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=Shops,
    returns_json=True,
    iterator="iter_find",
    item=_models.Shop,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)
_get_shop: Operation[Shop] = Operation(
    id="getShop",
    method="GET",
    path="/v3/application/shops/{shop_id}",
    resource="shops",
    name="get",
    params=(Param("shop_id", "shop_id", "path"),),
    response=Shop,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_shop_by_owner_user_id: Operation[Shop] = Operation(
    id="getShopByOwnerUserId",
    method="GET",
    path="/v3/application/users/{user_id}/shops",
    resource="shops",
    name="get_by_owner",
    params=(Param("user_id", "user_id", "path"),),
    response=Shop,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_shop: Operation[Shop] = Operation(
    id="updateShop",
    method="PUT",
    path="/v3/application/shops/{shop_id}",
    resource="shops",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("title", "title", "urlencoded"),
        Param("announcement", "announcement", "urlencoded"),
        Param("sale_message", "sale_message", "urlencoded"),
        Param("digital_sale_message", "digital_sale_message", "urlencoded"),
        Param("policy_additional", "policy_additional", "urlencoded"),
    ),
    response=Shop,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme(
                "oauth2",
                (
                    "shops_r",
                    "shops_w",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _find_shops,
    _get_shop,
    _get_shop_by_owner_user_id,
    _update_shop,
)


class ShopsApi(Resource):
    @checked
    def find(
        self,
        *,
        shop_name: StrictStr,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Shops:
        """Search one page of shops by name."""
        return self._call(
            _find_shops,
            shop_name=shop_name,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_find(
        self,
        *,
        shop_name: StrictStr,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.Shop]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_shops,
            shop_name=shop_name,
            limit=limit,
            offset=offset,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> Shop:
        """Get one shop."""
        return self._call(
            _get_shop,
            shop_id=shop_id,
        )

    @checked
    def get_by_owner(
        self,
        user_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> Shop:
        """Get the shop a user owns."""
        return self._call(
            _get_shop_by_owner_user_id,
            user_id=user_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: Optional[StrictStr] = None,
        announcement: Optional[StrictStr] = None,
        sale_message: Optional[StrictStr] = None,
        digital_sale_message: Optional[StrictStr] = None,
        policy_additional: Optional[StrictStr] = None,
    ) -> Shop:
        """Update a shop."""
        return self._call(
            _update_shop,
            shop_id=shop_id,
            title=title,
            announcement=announcement,
            sale_message=sale_message,
            digital_sale_message=digital_sale_message,
            policy_additional=policy_additional,
        )


class AsyncShopsApi(AsyncResource):
    @checked
    async def find(
        self,
        *,
        shop_name: StrictStr,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Shops:
        """Search one page of shops by name."""
        return await self._call(
            _find_shops,
            shop_name=shop_name,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_find(
        self,
        *,
        shop_name: StrictStr,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.Shop]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_shops,
            shop_name=shop_name,
            limit=limit,
            offset=offset,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> Shop:
        """Get one shop."""
        return await self._call(
            _get_shop,
            shop_id=shop_id,
        )

    @checked
    async def get_by_owner(
        self,
        user_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> Shop:
        """Get the shop a user owns."""
        return await self._call(
            _get_shop_by_owner_user_id,
            user_id=user_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: Optional[StrictStr] = None,
        announcement: Optional[StrictStr] = None,
        sale_message: Optional[StrictStr] = None,
        digital_sale_message: Optional[StrictStr] = None,
        policy_additional: Optional[StrictStr] = None,
    ) -> Shop:
        """Update a shop."""
        return await self._call(
            _update_shop,
            shop_id=shop_id,
            title=title,
            announcement=announcement,
            sale_message=sale_message,
            digital_sale_message=digital_sale_message,
            policy_additional=policy_additional,
        )
