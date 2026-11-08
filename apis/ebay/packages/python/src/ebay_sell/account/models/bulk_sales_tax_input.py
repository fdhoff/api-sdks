# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.sales_tax_input import SalesTaxInput
from ebay_sell._runtime import ApiModel


class BulkSalesTaxInput(ApiModel):
    """BulkSalesTaxInput model."""

    sales_tax_input_list: Optional[List[SalesTaxInput]] = Field(default=None, alias="salesTaxInputList")
