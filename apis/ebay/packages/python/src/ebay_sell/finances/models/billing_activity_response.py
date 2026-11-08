# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.billing_activity_line_item import BillingActivityLineItem
from ebay_sell._runtime import ApiModel


class BillingActivityResponse(ApiModel):
    """BillingActivityResponse model."""

    billing_activities: Optional[List[BillingActivityLineItem]] = Field(default=None, alias="billingActivities")
    count: Optional[StrictInt] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
