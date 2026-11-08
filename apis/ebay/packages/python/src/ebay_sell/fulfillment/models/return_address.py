# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.phone import Phone
from ebay_sell._runtime import ApiModel


class ReturnAddress(ApiModel):
    """ReturnAddress model."""

    address_line1: Optional[StrictStr] = Field(default=None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, alias="addressLine2")
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    county: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    primary_phone: Optional[Phone] = Field(default=None, alias="primaryPhone")
    state_or_province: Optional[StrictStr] = Field(default=None, alias="stateOrProvince")
