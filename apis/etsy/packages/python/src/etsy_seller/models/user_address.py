# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class UserAddress(ApiModel):
    """UserAddress model."""

    user_address_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    name: Optional[StrictStr] = None
    first_line: Optional[StrictStr] = None
    second_line: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    zip: Optional[StrictStr] = None
    iso_country_code: Optional[StrictStr] = None
    country_name: Optional[StrictStr] = None
    is_default_shipping_address: Optional[StrictBool] = None
