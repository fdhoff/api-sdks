# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.schedule_template_response import ScheduleTemplateResponse
from ebay_sell._runtime import ApiModel


class ScheduleTemplateCollection(ApiModel):
    """ScheduleTemplateCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    schedule_templates: Optional[List[ScheduleTemplateResponse]] = Field(default=None, alias="scheduleTemplates")
    total: Optional[StrictInt] = None
