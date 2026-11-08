# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class SalesTaxInput(ApiModel):
    """SalesTaxInput model."""

    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    sales_tax_jurisdiction_id: Optional[StrictStr] = Field(default=None, alias="salesTaxJurisdictionId")
    sales_tax_percentage: Optional[StrictStr] = Field(default=None, alias="salesTaxPercentage")
    shipping_and_handling_taxed: Optional[StrictBool] = Field(default=None, alias="shippingAndHandlingTaxed")
