# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell._runtime import ApiModel


class SellerFundsSummaryResponse(ApiModel):
    """SellerFundsSummaryResponse model."""

    available_funds: Optional[Amount] = Field(default=None, alias="availableFunds")
    funds_on_hold: Optional[Amount] = Field(default=None, alias="fundsOnHold")
    processing_funds: Optional[Amount] = Field(default=None, alias="processingFunds")
    total_funds: Optional[Amount] = Field(default=None, alias="totalFunds")
