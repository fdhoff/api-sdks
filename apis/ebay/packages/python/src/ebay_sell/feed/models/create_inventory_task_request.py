# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.inventory_filter_criteria import InventoryFilterCriteria
from ebay_sell._runtime import ApiModel


class CreateInventoryTaskRequest(ApiModel):
    """CreateInventoryTaskRequest model."""

    feed_type: Optional[StrictStr] = Field(default=None, alias="feedType")
    filter_criteria: Optional[InventoryFilterCriteria] = Field(default=None, alias="filterCriteria")
    schema_version: Optional[StrictStr] = Field(default=None, alias="schemaVersion")
