# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.escalation_eligibility_info import EscalationEligibilityInfo
from ebay_sell._runtime import ApiModel


class EscalationInfoType(ApiModel):
    """EscalationInfoType model."""

    buyer_escalation_eligibility_info: Optional[EscalationEligibilityInfo] = Field(
        default=None, alias="buyerEscalationEligibilityInfo"
    )
    case_id: Optional[StrictStr] = Field(default=None, alias="caseId")
    seller_escalation_eligibility_info: Optional[EscalationEligibilityInfo] = Field(
        default=None, alias="sellerEscalationEligibilityInfo"
    )
