# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.notification.models.subscription_payload_detail import SubscriptionPayloadDetail
from ebay_sell._runtime import ApiModel


class UpdateSubscriptionRequest(ApiModel):
    """UpdateSubscriptionRequest model."""

    destination_id: Optional[StrictStr] = Field(default=None, alias="destinationId")
    payload: Optional[SubscriptionPayloadDetail] = None
    status: Optional[StrictStr] = None
