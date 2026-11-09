# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Address(ApiModel):
    """Address model."""

    address_line1: Optional[StrictStr] = Field(default=None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, alias="addressLine2")
    address_type: Optional[StrictStr] = Field(default=None, alias="addressType")
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    county: Optional[StrictStr] = None
    is_transliterated: Optional[StrictBool] = Field(default=None, alias="isTransliterated")
    national_region: Optional[StrictStr] = Field(default=None, alias="nationalRegion")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    script: Optional[StrictStr] = None
    state_or_province: Optional[StrictStr] = Field(default=None, alias="stateOrProvince")
    transliterated_from_script: Optional[StrictStr] = Field(default=None, alias="transliteratedFromScript")
    world_region: Optional[StrictStr] = Field(default=None, alias="worldRegion")
