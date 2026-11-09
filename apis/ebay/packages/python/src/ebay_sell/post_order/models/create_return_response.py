# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.get_detail_response import GetDetailResponse
from ebay_sell.post_order.models.return_eligibility_per_item_type import ReturnEligibilityPerItemType
from ebay_sell.post_order.models.return_summary_type import ReturnSummaryType
from ebay_sell._runtime import ApiModel


class CreateReturnResponse(ApiModel):
    """CreateReturnResponse model."""

    detail: Optional[GetDetailResponse] = None
    eligibility_result: Optional[ReturnEligibilityPerItemType] = Field(default=None, alias="eligibilityResult")
    return_id: Optional[StrictStr] = Field(default=None, alias="returnId")
    summary: Optional[ReturnSummaryType] = None
