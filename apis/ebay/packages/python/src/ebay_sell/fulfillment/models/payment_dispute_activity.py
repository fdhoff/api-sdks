# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PaymentDisputeActivity(ApiModel):
    """PaymentDisputeActivity model."""

    activity_date: Optional[StrictStr] = Field(default=None, alias="activityDate")
    activity_type: Optional[StrictStr] = Field(default=None, alias="activityType")
    actor: Optional[StrictStr] = None
