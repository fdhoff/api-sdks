# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.promotion_report_detail import PromotionReportDetail
from ebay_sell._runtime import ApiModel


class PromotionsReportPagedCollection(ApiModel):
    """PromotionsReportPagedCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    promotion_reports: Optional[List[PromotionReportDetail]] = Field(default=None, alias="promotionReports")
    total: Optional[StrictInt] = None
