# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.inventory_filter_criteria import InventoryFilterCriteria
from ebay_sell.feed.models.upload_summary import UploadSummary
from ebay_sell._runtime import ApiModel


class InventoryTask(ApiModel):
    """InventoryTask model."""

    task_id: Optional[StrictStr] = Field(default=None, alias="taskId")
    status: Optional[StrictStr] = None
    feed_type: Optional[StrictStr] = Field(default=None, alias="feedType")
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    completion_date: Optional[StrictStr] = Field(default=None, alias="completionDate")
    schema_version: Optional[StrictStr] = Field(default=None, alias="schemaVersion")
    detail_href: Optional[StrictStr] = Field(default=None, alias="detailHref")
    upload_summary: Optional[UploadSummary] = Field(default=None, alias="uploadSummary")
    filter_criteria: Optional[InventoryFilterCriteria] = Field(default=None, alias="filterCriteria")
