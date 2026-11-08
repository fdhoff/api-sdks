# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopEconomicOperator(ApiModel):
    """ShopEconomicOperator model."""

    economic_operator_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    operator_name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    trademark_name: Optional[StrictStr] = None
    first_line: Optional[StrictStr] = None
    second_line: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    zip: Optional[StrictStr] = None
    country_iso: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    phone_country_iso: Optional[StrictStr] = None
    create_date: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    update_date: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
