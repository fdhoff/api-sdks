# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.sales_tax_jurisdiction import SalesTaxJurisdiction
from ebay_sell._runtime import ApiModel


class SalesTaxJurisdictions(ApiModel):
    """SalesTaxJurisdictions model."""

    sales_tax_jurisdictions: Optional[List[SalesTaxJurisdiction]] = Field(default=None, alias="salesTaxJurisdictions")
