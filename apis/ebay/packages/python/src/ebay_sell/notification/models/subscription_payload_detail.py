# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class SubscriptionPayloadDetail(ApiModel):
    """SubscriptionPayloadDetail model."""

    delivery_protocol: Optional[StrictStr] = Field(default=None, alias="deliveryProtocol")
    format: Optional[StrictStr] = None
    schema_version: Optional[StrictStr] = Field(default=None, alias="schemaVersion")
