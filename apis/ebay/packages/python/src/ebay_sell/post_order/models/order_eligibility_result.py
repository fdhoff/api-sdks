# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.item_eligibility_result import ItemEligibilityResult
from ebay_sell._runtime import ApiModel


class OrderEligibilityResult(ApiModel):
    """OrderEligibilityResult model."""

    eligible: Optional[StrictBool] = None
    eligible_cancel_reason: Optional[List[StrictStr]] = Field(default=None, alias="eligibleCancelReason")
    failure_reason: Optional[List[StrictStr]] = Field(default=None, alias="failureReason")
    item_eligibility_result: Optional[List[ItemEligibilityResult]] = Field(default=None, alias="itemEligibilityResult")
    legacy_order_id: Optional[StrictStr] = Field(default=None, alias="legacyOrderId")
