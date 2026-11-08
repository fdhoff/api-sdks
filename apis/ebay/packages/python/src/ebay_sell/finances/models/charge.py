# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell._runtime import ApiModel


class Charge(ApiModel):
    """Charge model."""

    cancellation_id: Optional[StrictStr] = Field(default=None, alias="cancellationId")
    case_id: Optional[StrictStr] = Field(default=None, alias="caseId")
    charge_net_amount: Optional[Amount] = Field(default=None, alias="chargeNetAmount")
    inquiry_id: Optional[StrictStr] = Field(default=None, alias="inquiryId")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    payment_dispute_id: Optional[StrictStr] = Field(default=None, alias="paymentDisputeId")
    refund_id: Optional[StrictStr] = Field(default=None, alias="refundId")
    return_id: Optional[StrictStr] = Field(default=None, alias="returnId")
