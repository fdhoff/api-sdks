# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.report_metadata import ReportMetadata
from ebay_sell._runtime import ApiModel


class ReportMetadatas(ApiModel):
    """ReportMetadatas model."""

    report_metadata: Optional[List[ReportMetadata]] = Field(default=None, alias="reportMetadata")
