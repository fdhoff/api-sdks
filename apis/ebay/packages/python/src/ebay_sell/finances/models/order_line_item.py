# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.fee import Fee
from ebay_sell._runtime import ApiModel


class OrderLineItem(ApiModel):
    """OrderLineItem model."""

    donations: Optional[List[Fee]] = None
    fee_basis_amount: Optional[Amount] = Field(default=None, alias="feeBasisAmount")
    line_item_id: Optional[StrictStr] = Field(default=None, alias="lineItemId")
    marketplace_fees: Optional[List[Fee]] = Field(default=None, alias="marketplaceFees")
