# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_detail_type import ReturnDetailType
from ebay_sell.post_order.models.return_summary_type import ReturnSummaryType
from ebay_sell._runtime import ApiModel


class GetDetailResponse(ApiModel):
    """GetDetailResponse model."""

    detail: Optional[ReturnDetailType] = None
    summary: Optional[ReturnSummaryType] = None
