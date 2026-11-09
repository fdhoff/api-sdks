# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.webhook_event_type import WebhookEventType
from mercury_banking._runtime import ApiModel


class VerifyWebhookParams(ApiModel):
    """VerifyWebhookParams model."""

    event_type: Optional[WebhookEventType] = Field(default=None, alias="eventType")
