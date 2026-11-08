# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_production_partners import ShopProductionPartners

_get_shop_production_partners: Operation[ShopProductionPartners] = Operation(
    id="getShopProductionPartners",
    method="GET",
    path="/v3/application/shops/{shop_id}/production-partners",
    resource="production_partners",
    name="list",
    params=(Param("shop_id", "shop_id", "path"),),
    response=ShopProductionPartners,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)

OPERATIONS = (_get_shop_production_partners,)


class ProductionPartnersApi(Resource):
    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopProductionPartners:
        """List a shop&#39;s production partners."""
        return self._call(
            _get_shop_production_partners,
            shop_id=shop_id,
        )


class AsyncProductionPartnersApi(AsyncResource):
    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopProductionPartners:
        """List a shop&#39;s production partners."""
        return await self._call(
            _get_shop_production_partners,
            shop_id=shop_id,
        )
