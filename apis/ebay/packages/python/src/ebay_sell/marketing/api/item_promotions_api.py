# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing.models.base_response import BaseResponse
from ebay_sell.marketing.models.item_promotion import ItemPromotion
from ebay_sell.marketing.models.item_promotion_response import ItemPromotionResponse

_create_item_promotion: Operation[BaseResponse] = Operation(
    id="createItemPromotion",
    method="POST",
    path="/sell/marketing/v1/item_promotion",
    resource="item_promotions",
    name="create",
    params=(),
    response=BaseResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_item_promotion: Operation[None] = Operation(
    id="deleteItemPromotion",
    method="DELETE",
    path="/sell/marketing/v1/item_promotion/{promotion_id}",
    resource="item_promotions",
    name="delete",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_item_promotion: Operation[ItemPromotionResponse] = Operation(
    id="getItemPromotion",
    method="GET",
    path="/sell/marketing/v1/item_promotion/{promotion_id}",
    resource="item_promotions",
    name="get",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=ItemPromotionResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_update_item_promotion: Operation[BaseResponse] = Operation(
    id="updateItemPromotion",
    method="PUT",
    path="/sell/marketing/v1/item_promotion/{promotion_id}",
    resource="item_promotions",
    name="update",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=BaseResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _create_item_promotion,
    _delete_item_promotion,
    _get_item_promotion,
    _update_item_promotion,
)


class ItemPromotionsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[ItemPromotion, Mapping[str, Any]]] = None,
    ) -> BaseResponse:
        """Create a threshold promotion."""
        return self._call(
            _create_item_promotion,
            _body=body,
        )

    @checked
    def delete(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Delete a threshold promotion."""
        return self._call(
            _delete_item_promotion,
            promotion_id=promotion_id,
        )

    @checked
    def get(
        self,
        promotion_id: StrictStr,
    ) -> ItemPromotionResponse:
        """Get one threshold promotion."""
        return self._call(
            _get_item_promotion,
            promotion_id=promotion_id,
        )

    @checked
    def update(
        self,
        promotion_id: StrictStr,
        body: Optional[Union[ItemPromotion, Mapping[str, Any]]] = None,
    ) -> BaseResponse:
        """Replace a threshold promotion."""
        return self._call(
            _update_item_promotion,
            promotion_id=promotion_id,
            _body=body,
        )


class AsyncItemPromotionsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[ItemPromotion, Mapping[str, Any]]] = None,
    ) -> BaseResponse:
        """Create a threshold promotion."""
        return await self._call(
            _create_item_promotion,
            _body=body,
        )

    @checked
    async def delete(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Delete a threshold promotion."""
        return await self._call(
            _delete_item_promotion,
            promotion_id=promotion_id,
        )

    @checked
    async def get(
        self,
        promotion_id: StrictStr,
    ) -> ItemPromotionResponse:
        """Get one threshold promotion."""
        return await self._call(
            _get_item_promotion,
            promotion_id=promotion_id,
        )

    @checked
    async def update(
        self,
        promotion_id: StrictStr,
        body: Optional[Union[ItemPromotion, Mapping[str, Any]]] = None,
    ) -> BaseResponse:
        """Replace a threshold promotion."""
        return await self._call(
            _update_item_promotion,
            promotion_id=promotion_id,
            _body=body,
        )
