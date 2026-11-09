# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.error_data import ErrorData
from ebay_sell.post_order.models.order_eligibility_result import OrderEligibilityResult
from ebay_sell._runtime import ApiModel


class CreateCancelResponse(ApiModel):
    """CreateCancelResponse model."""

    cancel_id: Optional[StrictStr] = Field(default=None, alias="cancelId")
    order_eligibility_result: Optional[OrderEligibilityResult] = Field(default=None, alias="orderEligibilityResult")
    warnings: Optional[List[ErrorData]] = None
