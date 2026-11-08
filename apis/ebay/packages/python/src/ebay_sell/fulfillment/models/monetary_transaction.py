# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.dispute_amount import DisputeAmount
from ebay_sell._runtime import ApiModel


class MonetaryTransaction(ApiModel):
    """MonetaryTransaction model."""

    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    type: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    amount: Optional[DisputeAmount] = None
