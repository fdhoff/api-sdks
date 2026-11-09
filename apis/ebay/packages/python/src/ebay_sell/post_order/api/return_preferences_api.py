# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.post_order.models.get_seller_return_preference_response import GetSellerReturnPreferenceResponse
from ebay_sell.post_order.models.set_seller_return_preference_request import SetSellerReturnPreferenceRequest

_get_return_preferences: Operation[GetSellerReturnPreferenceResponse] = Operation(
    id="getReturnPreferences",
    method="GET",
    path="/post-order/v2/return/preference",
    resource="return_preferences",
    name="get",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=GetSellerReturnPreferenceResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_set_return_preferences: Operation[object] = Operation(
    id="setReturnPreferences",
    method="POST",
    path="/post-order/v2/return/preference",
    resource="return_preferences",
    name="set",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_return_preferences,
    _set_return_preferences,
)


class ReturnPreferencesApi(Resource):
    @checked
    def get(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetSellerReturnPreferenceResponse:
        """Get the seller's return preferences."""
        return self._call(
            _get_return_preferences,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def set(
        self,
        body: Union[SetSellerReturnPreferenceRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Set the seller's return preferences."""
        return self._call(
            _set_return_preferences,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncReturnPreferencesApi(AsyncResource):
    @checked
    async def get(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetSellerReturnPreferenceResponse:
        """Get the seller's return preferences."""
        return await self._call(
            _get_return_preferences,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def set(
        self,
        body: Union[SetSellerReturnPreferenceRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Set the seller's return preferences."""
        return await self._call(
            _set_return_preferences,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
