# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.fee_summary import FeeSummary
from ebay_sell._runtime import ApiModel


class FeesSummaryResponse(ApiModel):
    """FeesSummaryResponse model."""

    fee_summaries: Optional[List[FeeSummary]] = Field(default=None, alias="feeSummaries")
