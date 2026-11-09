# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.cancel_summary import CancelSummary
from ebay_sell.post_order.models.pagination_output import PaginationOutput
from ebay_sell._runtime import ApiModel


class FindCancelResponse(ApiModel):
    """FindCancelResponse model."""

    cancellations: Optional[List[CancelSummary]] = None
    pagination_output: Optional[PaginationOutput] = Field(default=None, alias="paginationOutput")
    total: Optional[StrictInt] = None
