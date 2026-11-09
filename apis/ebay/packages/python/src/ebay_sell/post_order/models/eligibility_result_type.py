# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_eligibility_error_detail_type import ReturnEligibilityErrorDetailType
from ebay_sell.post_order.models.status_type import StatusType
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class EligibilityResultType(ApiModel):
    """EligibilityResultType model."""

    case_id: Optional[StrictStr] = Field(default=None, alias="caseId")
    eligibility_error_detail: Optional[List[ReturnEligibilityErrorDetailType]] = Field(
        default=None, alias="eligibilityErrorDetail"
    )
    eligibility_status: Optional[StatusType] = Field(default=None, alias="eligibilityStatus")
    eligible_start_date: Optional[Timestamp] = Field(default=None, alias="eligibleStartDate")
    return_creation_date: Optional[Timestamp] = Field(default=None, alias="returnCreationDate")
    return_deadline: Optional[Timestamp] = Field(default=None, alias="returnDeadline")
    return_id: Optional[StrictStr] = Field(default=None, alias="returnId")
