# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.funding_source import FundingSource
from ebay_sell.finances.models.transfer_detail import TransferDetail
from ebay_sell._runtime import ApiModel


class Transfer(ApiModel):
    """Transfer model."""

    funding_source: Optional[FundingSource] = Field(default=None, alias="fundingSource")
    transaction_date: Optional[StrictStr] = Field(default=None, alias="transactionDate")
    transfer_amount: Optional[Amount] = Field(default=None, alias="transferAmount")
    transfer_detail: Optional[TransferDetail] = Field(default=None, alias="transferDetail")
    transfer_id: Optional[StrictStr] = Field(default=None, alias="transferId")
