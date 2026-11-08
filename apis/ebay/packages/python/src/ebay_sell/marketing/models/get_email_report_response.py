# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class GetEmailReportResponse(ApiModel):
    """GetEmailReportResponse model."""

    click_count: Optional[StrictInt] = Field(default=None, alias="clickCount")
    open_count: Optional[StrictInt] = Field(default=None, alias="openCount")
    total_sales: Optional[Amount] = Field(default=None, alias="totalSales")
