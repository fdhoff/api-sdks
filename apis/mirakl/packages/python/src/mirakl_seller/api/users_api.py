# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictInt

from mirakl_seller._runtime import (
    AsyncResource,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.ro02_response200 import RO02Response200

_r_o02: Operation[RO02Response200] = Operation(
    id="RO02",
    method="GET",
    path="/api/users/shops/roles",
    resource="users",
    name="list_shop_roles",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RO02Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_SHOP_USER_CREATE",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)

OPERATIONS = (_r_o02,)


class UsersApi(Resource):
    @checked
    def list_shop_roles(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RO02Response200:
        """List the shop roles (RO02)."""
        return self._call(
            _r_o02,
            shop_id=shop_id,
        )


class AsyncUsersApi(AsyncResource):
    @checked
    async def list_shop_roles(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RO02Response200:
        """List the shop roles (RO02)."""
        return await self._call(
            _r_o02,
            shop_id=shop_id,
        )
