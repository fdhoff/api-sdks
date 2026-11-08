# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell._runtime import ApiModel


class Tax(ApiModel):
    """Tax model."""

    amount: Optional[Amount] = None
    tax_type: Optional[StrictStr] = Field(default=None, alias="taxType")
