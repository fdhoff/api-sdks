# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking.models.payment_approval_review_status import PaymentApprovalReviewStatus
from mercury_banking._runtime import ApiModel


class PaymentApprovalReview(ApiModel):
    """PaymentApprovalReview model."""

    reviewed_at: StrictStr = Field(alias="reviewedAt")
    reviewer_user_id: UUID = Field(alias="reviewerUserId")
    status: PaymentApprovalReviewStatus
