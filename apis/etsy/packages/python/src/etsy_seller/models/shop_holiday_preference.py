# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopHolidayPreference(ApiModel):
    """ShopHolidayPreference model."""

    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    holiday_id: Optional[StrictInt] = None
    country_iso: Optional[StrictStr] = None
    is_working: Optional[StrictBool] = None
    holiday_name: Optional[StrictStr] = None
