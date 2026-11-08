# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.seller_eligibility_response import SellerEligibilityResponse
from ebay_sell._runtime import ApiModel


class SellerEligibilityMultiProgramResponse(ApiModel):
    """SellerEligibilityMultiProgramResponse model."""

    advertising_eligibility: Optional[List[SellerEligibilityResponse]] = Field(
        default=None, alias="advertisingEligibility"
    )
