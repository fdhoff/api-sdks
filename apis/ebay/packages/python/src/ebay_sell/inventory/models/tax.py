# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Tax(ApiModel):
    """Tax model."""

    apply_tax: Optional[StrictBool] = Field(default=None, alias="applyTax")
    third_party_tax_category: Optional[StrictStr] = Field(default=None, alias="thirdPartyTaxCategory")
    vat_percentage: Optional[float] = Field(default=None, alias="vatPercentage")
