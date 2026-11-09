# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.count_summary_type import CountSummaryType
from ebay_sell.post_order.models.pagination_output import PaginationOutput
from ebay_sell.post_order.models.return_summary_type import ReturnSummaryType
from ebay_sell._runtime import ApiModel


class GetSummaryResponse(ApiModel):
    """GetSummaryResponse model."""

    count_summary: Optional[List[CountSummaryType]] = Field(default=None, alias="countSummary")
    members: Optional[List[ReturnSummaryType]] = None
    pagination_output: Optional[PaginationOutput] = Field(default=None, alias="paginationOutput")
    total: Optional[StrictInt] = None
