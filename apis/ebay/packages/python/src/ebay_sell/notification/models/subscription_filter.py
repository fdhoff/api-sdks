# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class SubscriptionFilter(ApiModel):
    """SubscriptionFilter model."""

    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    filter_id: Optional[StrictStr] = Field(default=None, alias="filterId")
    filter_schema: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="filterSchema")
    filter_status: Optional[StrictStr] = Field(default=None, alias="filterStatus")
    subscription_id: Optional[StrictStr] = Field(default=None, alias="subscriptionId")
