# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class Subscription(ApiModel):
    """Subscription model."""

    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    subscription_id: Optional[StrictStr] = Field(default=None, alias="subscriptionId")
    subscription_level: Optional[StrictStr] = Field(default=None, alias="subscriptionLevel")
    subscription_type: Optional[StrictStr] = Field(default=None, alias="subscriptionType")
    term: Optional[TimeDuration] = None
