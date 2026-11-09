# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_eligibility_item_per_check_type_result import (
    ReturnEligibilityItemPerCheckTypeResult,
)
from ebay_sell.post_order.models.return_eligibility_item_type import ReturnEligibilityItemType
from ebay_sell._runtime import ApiModel


class ReturnEligibilityPerItemType(ApiModel):
    """ReturnEligibilityPerItemType model."""

    eligibility_results_per_check_type: Optional[List[ReturnEligibilityItemPerCheckTypeResult]] = Field(
        default=None, alias="eligibilityResultsPerCheckType"
    )
    return_item: Optional[ReturnEligibilityItemType] = Field(default=None, alias="returnItem")
