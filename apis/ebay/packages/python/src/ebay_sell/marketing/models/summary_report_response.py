# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class SummaryReportResponse(ApiModel):
    """SummaryReportResponse model."""

    base_sale: Optional[Amount] = Field(default=None, alias="baseSale")
    last_updated: Optional[StrictStr] = Field(default=None, alias="lastUpdated")
    percentage_sales_lift: Optional[StrictStr] = Field(default=None, alias="percentageSalesLift")
    promotion_sale: Optional[Amount] = Field(default=None, alias="promotionSale")
    total_sale: Optional[Amount] = Field(default=None, alias="totalSale")
