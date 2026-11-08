# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.updated_sales_tax_entry import UpdatedSalesTaxEntry
from ebay_sell._runtime import ApiModel


class UpdatedSalesTaxResponse(ApiModel):
    """UpdatedSalesTaxResponse model."""

    updated_sales_tax_entries: Optional[List[UpdatedSalesTaxEntry]] = Field(
        default=None, alias="updatedSalesTaxEntries"
    )
