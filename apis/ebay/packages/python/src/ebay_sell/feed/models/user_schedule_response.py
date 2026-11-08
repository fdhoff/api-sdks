# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class UserScheduleResponse(ApiModel):
    """UserScheduleResponse model."""

    schedule_id: Optional[StrictStr] = Field(default=None, alias="scheduleId")
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    feed_type: Optional[StrictStr] = Field(default=None, alias="feedType")
    last_modified_date: Optional[StrictStr] = Field(default=None, alias="lastModifiedDate")
    preferred_trigger_day_of_month: Optional[StrictInt] = Field(default=None, alias="preferredTriggerDayOfMonth")
    preferred_trigger_day_of_week: Optional[StrictStr] = Field(default=None, alias="preferredTriggerDayOfWeek")
    preferred_trigger_hour: Optional[StrictStr] = Field(default=None, alias="preferredTriggerHour")
    schedule_end_date: Optional[StrictStr] = Field(default=None, alias="scheduleEndDate")
    schedule_name: Optional[StrictStr] = Field(default=None, alias="scheduleName")
    schedule_start_date: Optional[StrictStr] = Field(default=None, alias="scheduleStartDate")
    schedule_template_id: Optional[StrictStr] = Field(default=None, alias="scheduleTemplateId")
    schema_version: Optional[StrictStr] = Field(default=None, alias="schemaVersion")
    status: Optional[StrictStr] = None
    status_reason: Optional[StrictStr] = Field(default=None, alias="statusReason")
