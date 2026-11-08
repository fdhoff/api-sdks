# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.fee import Fee
from ebay_sell.finances.models.payout_instrument import PayoutInstrument
from ebay_sell._runtime import ApiModel


class Payout(ApiModel):
    """Payout model."""

    amount: Optional[Amount] = None
    bank_reference: Optional[StrictStr] = Field(default=None, alias="bankReference")
    last_attempted_payout_date: Optional[StrictStr] = Field(default=None, alias="lastAttemptedPayoutDate")
    payout_date: Optional[StrictStr] = Field(default=None, alias="payoutDate")
    payout_id: Optional[StrictStr] = Field(default=None, alias="payoutId")
    payout_instrument: Optional[PayoutInstrument] = Field(default=None, alias="payoutInstrument")
    payout_memo: Optional[StrictStr] = Field(default=None, alias="payoutMemo")
    payout_reference: Optional[StrictStr] = Field(default=None, alias="payoutReference")
    payout_status: Optional[StrictStr] = Field(default=None, alias="payoutStatus")
    payout_status_description: Optional[StrictStr] = Field(default=None, alias="payoutStatusDescription")
    total_amount: Optional[Amount] = Field(default=None, alias="totalAmount")
    total_fee: Optional[Amount] = Field(default=None, alias="totalFee")
    total_fee_details: Optional[List[Fee]] = Field(default=None, alias="totalFeeDetails")
    transaction_count: Optional[StrictInt] = Field(default=None, alias="transactionCount")
