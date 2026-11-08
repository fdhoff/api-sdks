# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.simple_amount import SimpleAmount
from ebay_sell._runtime import ApiModel


class PaymentDisputeOutcomeDetail(ApiModel):
    """PaymentDisputeOutcomeDetail model."""

    fees: Optional[SimpleAmount] = None
    protected_amount: Optional[SimpleAmount] = Field(default=None, alias="protectedAmount")
    protection_status: Optional[StrictStr] = Field(default=None, alias="protectionStatus")
    reason_for_closure: Optional[StrictStr] = Field(default=None, alias="reasonForClosure")
    recoup_amount: Optional[SimpleAmount] = Field(default=None, alias="recoupAmount")
    total_fee_credit: Optional[SimpleAmount] = Field(default=None, alias="totalFeeCredit")
