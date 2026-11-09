# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.funding_source_type import FundingSourceType
from ebay_sell.post_order.models.funding_status_enum import FundingStatusEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class RefundFundingType(ApiModel):
    """RefundFundingType model."""

    var_date: Optional[Timestamp] = Field(default=None, alias="date")
    amount: Optional[Amount] = None
    funding_source: Optional[FundingSourceType] = Field(default=None, alias="fundingSource")
    funding_status: Optional[FundingStatusEnum] = Field(default=None, alias="fundingStatus")
