# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.api_v1_reimbursement_attachment import ApiV1ReimbursementAttachment
from mercury_banking.models.reimbursement_payment_status import ReimbursementPaymentStatus
from mercury_banking.models.reimbursement_review_status import ReimbursementReviewStatus
from mercury_banking._runtime import ApiModel


class ApiV1ReimbursementListItem(ApiModel):
    """ApiV1ReimbursementListItem model."""

    amount: Annotated[float, Field(multiple_of=0.01)]
    attachments: List[ApiV1ReimbursementAttachment]
    currency: StrictStr
    id: UUID
    payment_status: ReimbursementPaymentStatus = Field(alias="paymentStatus")
    review_status: ReimbursementReviewStatus = Field(alias="reviewStatus")
    submitted_at: StrictStr = Field(alias="submittedAt")
    submitter_user_id: UUID = Field(alias="submitterUserId")
