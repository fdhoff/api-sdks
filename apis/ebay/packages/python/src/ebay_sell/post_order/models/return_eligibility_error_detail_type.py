# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.eligibility_error_type import EligibilityErrorType
from ebay_sell._runtime import ApiModel


class ReturnEligibilityErrorDetailType(ApiModel):
    """ReturnEligibilityErrorDetailType model."""

    eligibility_error: Optional[EligibilityErrorType] = Field(default=None, alias="eligibilityError")
