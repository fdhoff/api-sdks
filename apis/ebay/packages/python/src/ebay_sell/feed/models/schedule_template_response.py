# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.supported_configuration import SupportedConfiguration
from ebay_sell._runtime import ApiModel


class ScheduleTemplateResponse(ApiModel):
    """ScheduleTemplateResponse model."""

    feed_type: Optional[StrictStr] = Field(default=None, alias="feedType")
    frequency: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    schedule_template_id: Optional[StrictStr] = Field(default=None, alias="scheduleTemplateId")
    status: Optional[StrictStr] = None
    supported_configurations: Optional[List[SupportedConfiguration]] = Field(
        default=None, alias="supportedConfigurations"
    )
