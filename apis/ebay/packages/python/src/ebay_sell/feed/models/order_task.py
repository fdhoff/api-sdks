# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.order_filter_criteria import OrderFilterCriteria
from ebay_sell.feed.models.upload_summary import UploadSummary
from ebay_sell._runtime import ApiModel


class OrderTask(ApiModel):
    """OrderTask model."""

    completion_date: Optional[StrictStr] = Field(default=None, alias="completionDate")
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    detail_href: Optional[StrictStr] = Field(default=None, alias="detailHref")
    feed_type: Optional[StrictStr] = Field(default=None, alias="feedType")
    filter_criteria: Optional[OrderFilterCriteria] = Field(default=None, alias="filterCriteria")
    schema_version: Optional[StrictStr] = Field(default=None, alias="schemaVersion")
    status: Optional[StrictStr] = None
    task_id: Optional[StrictStr] = Field(default=None, alias="taskId")
    upload_summary: Optional[UploadSummary] = Field(default=None, alias="uploadSummary")
