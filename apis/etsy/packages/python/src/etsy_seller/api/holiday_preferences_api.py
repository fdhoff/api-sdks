# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List

from pydantic import Field, StrictBool, StrictInt
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_holiday_preference import ShopHolidayPreference

_get_holiday_preferences: Operation[List[ShopHolidayPreference]] = Operation(
    id="getHolidayPreferences",
    method="GET",
    path="/v3/application/shops/{shop_id}/holiday-preferences",
    resource="holiday_preferences",
    name="list",
    params=(Param("shop_id", "shop_id", "path"),),
    response=List[ShopHolidayPreference],
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_update_holiday_preferences: Operation[ShopHolidayPreference] = Operation(
    id="updateHolidayPreferences",
    method="PUT",
    path="/v3/application/shops/{shop_id}/holiday-preferences/{holiday_id}",
    resource="holiday_preferences",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("holiday_id", "holiday_id", "path"),
        Param("is_working", "is_working", "urlencoded"),
    ),
    response=ShopHolidayPreference,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)

OPERATIONS = (
    _get_holiday_preferences,
    _update_holiday_preferences,
)


class HolidayPreferencesApi(Resource):
    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> List[ShopHolidayPreference]:
        """List a shop&#39;s holiday preferences."""
        return self._call(
            _get_holiday_preferences,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        holiday_id: StrictInt,
        *,
        is_working: StrictBool,
    ) -> ShopHolidayPreference:
        """Update a shop&#39;s preference for one holiday."""
        return self._call(
            _update_holiday_preferences,
            shop_id=shop_id,
            holiday_id=holiday_id,
            is_working=is_working,
        )


class AsyncHolidayPreferencesApi(AsyncResource):
    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> List[ShopHolidayPreference]:
        """List a shop&#39;s holiday preferences."""
        return await self._call(
            _get_holiday_preferences,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        holiday_id: StrictInt,
        *,
        is_working: StrictBool,
    ) -> ShopHolidayPreference:
        """Update a shop&#39;s preference for one holiday."""
        return await self._call(
            _update_holiday_preferences,
            shop_id=shop_id,
            holiday_id=holiday_id,
            is_working=is_working,
        )
