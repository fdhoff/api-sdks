# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.eligibility_result_type import EligibilityResultType
from ebay_sell.post_order.models.ret_eligibility_check_type_enum import RetEligibilityCheckTypeEnum
from ebay_sell._runtime import ApiModel


class ReturnEligibilityItemPerCheckTypeResult(ApiModel):
    """ReturnEligibilityItemPerCheckTypeResult model."""

    check_type: Optional[RetEligibilityCheckTypeEnum] = Field(default=None, alias="checkType")
    eligibility_info: Optional[EligibilityResultType] = Field(default=None, alias="eligibilityInfo")
