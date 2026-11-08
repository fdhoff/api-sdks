# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.date_range import DateRange
from ebay_sell._runtime import ApiModel


class OrderFilterCriteria(ApiModel):
    """OrderFilterCriteria model."""

    creation_date_range: Optional[DateRange] = Field(default=None, alias="creationDateRange")
    modified_date_range: Optional[DateRange] = Field(default=None, alias="modifiedDateRange")
    order_status: Optional[StrictStr] = Field(default=None, alias="orderStatus")
