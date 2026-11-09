# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class SwiftCodeData(ApiModel):
    """SwiftCodeData model."""

    bank_city_state: StrictStr = Field(alias="bankCityState")
    bank_country: StrictStr = Field(alias="bankCountry")
    bank_name: StrictStr = Field(alias="bankName")
