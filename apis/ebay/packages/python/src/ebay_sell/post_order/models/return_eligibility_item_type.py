# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ReturnEligibilityItemType(ApiModel):
    """ReturnEligibilityItemType model."""

    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    reason: Optional[StrictStr] = None
    return_quantity: Optional[StrictInt] = Field(default=None, alias="returnQuantity")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
