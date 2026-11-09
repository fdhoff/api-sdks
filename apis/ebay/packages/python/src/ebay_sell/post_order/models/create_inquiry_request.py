# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.desired_outcome_type_enum import DesiredOutcomeTypeEnum
from ebay_sell.post_order.models.text import Text
from ebay_sell._runtime import ApiModel


class CreateInquiryRequest(ApiModel):
    """CreateInquiryRequest model."""

    claim_quantity: Optional[StrictInt] = Field(default=None, alias="claimQuantity")
    comments: Optional[Text] = None
    desired_outcome: Optional[DesiredOutcomeTypeEnum] = Field(default=None, alias="desiredOutcome")
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
