# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ItemEligibilityResult(ApiModel):
    """ItemEligibilityResult model."""

    cancel_quantity: Optional[StrictInt] = Field(default=None, alias="cancelQuantity")
    eligible: Optional[StrictBool] = None
    failure_reason: Optional[List[StrictStr]] = Field(default=None, alias="failureReason")
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
