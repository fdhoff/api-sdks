# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.error import Error
from ebay_sell.analytics.models.header import Header
from ebay_sell.analytics.models.metadata import Metadata
from ebay_sell.analytics.models.record import Record
from ebay_sell._runtime import ApiModel


class Report(ApiModel):
    """Report model."""

    dimension_metadata: Optional[List[Metadata]] = Field(default=None, alias="dimensionMetadata")
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    header: Optional[Header] = None
    last_updated_date: Optional[StrictStr] = Field(default=None, alias="lastUpdatedDate")
    records: Optional[List[Record]] = None
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
    warnings: Optional[List[Error]] = None
