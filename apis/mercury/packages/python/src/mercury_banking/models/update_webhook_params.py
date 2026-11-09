# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.resource_field import ResourceField
from mercury_banking.models.webhook_event_type import WebhookEventType
from mercury_banking.models.webhook_update_status import WebhookUpdateStatus
from mercury_banking._runtime import ApiModel


class UpdateWebhookParams(ApiModel):
    """UpdateWebhookParams model."""

    event_types: Optional[List[WebhookEventType]] = Field(default=None, alias="eventTypes")
    filter_paths: Optional[List[ResourceField]] = Field(default=None, alias="filterPaths")
    status: Optional[WebhookUpdateStatus] = None
    url: Optional[StrictStr] = None
