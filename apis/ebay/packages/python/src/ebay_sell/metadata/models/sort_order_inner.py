# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.sort_order_properties import SortOrderProperties
from ebay_sell._runtime import ApiModel


class SortOrderInner(ApiModel):
    """SortOrderInner model."""

    sort_order: Optional[SortOrderProperties] = Field(default=None, alias="sortOrder")
    sort_priority: Optional[StrictStr] = Field(default=None, alias="sortPriority")
