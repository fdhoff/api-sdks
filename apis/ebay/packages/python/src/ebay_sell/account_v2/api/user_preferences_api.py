# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account_v2.models.get_user_preferences_response import GetUserPreferencesResponse

_get_user_preferences: Operation[GetUserPreferencesResponse] = Operation(
    id="getUserPreferences",
    method="GET",
    path="/sell/account/v2/user_preferences",
    resource="user_preferences",
    name="get",
    params=(
        Param("fieldgroups", "fieldgroups", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=GetUserPreferencesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account.readonly",)),),),
    host="api",
)
_set_user_preferences: Operation[None] = Operation(
    id="setUserPreferences",
    method="PATCH",
    path="/sell/account/v2/user_preferences",
    resource="user_preferences",
    name="set",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _get_user_preferences,
    _set_user_preferences,
)


class UserPreferencesApi(Resource):
    @checked
    def get(
        self,
        *,
        fieldgroups: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetUserPreferencesResponse:
        """Get the seller's account preferences."""
        return self._call(
            _get_user_preferences,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def set(
        self,
        body: Optional[Union[Dict[str, object], Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update the seller's account preferences."""
        return self._call(
            _set_user_preferences,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncUserPreferencesApi(AsyncResource):
    @checked
    async def get(
        self,
        *,
        fieldgroups: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetUserPreferencesResponse:
        """Get the seller's account preferences."""
        return await self._call(
            _get_user_preferences,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def set(
        self,
        body: Optional[Union[Dict[str, object], Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Update the seller's account preferences."""
        return await self._call(
            _set_user_preferences,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
