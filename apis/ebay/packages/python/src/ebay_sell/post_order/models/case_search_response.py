# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.case_summary_type import CaseSummaryType
from ebay_sell.post_order.models.pagination_output import PaginationOutput
from ebay_sell._runtime import ApiModel


class CaseSearchResponse(ApiModel):
    """CaseSearchResponse model."""

    members: Optional[List[CaseSummaryType]] = None
    pagination_output: Optional[PaginationOutput] = Field(default=None, alias="paginationOutput")
    total_number_of_cases: Optional[StrictInt] = Field(default=None, alias="totalNumberOfCases")
