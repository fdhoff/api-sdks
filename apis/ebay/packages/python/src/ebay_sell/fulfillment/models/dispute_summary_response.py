# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.payment_dispute_summary import PaymentDisputeSummary
from ebay_sell._runtime import ApiModel


class DisputeSummaryResponse(ApiModel):
    """DisputeSummaryResponse model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    payment_dispute_summaries: Optional[List[PaymentDisputeSummary]] = Field(
        default=None, alias="paymentDisputeSummaries"
    )
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
