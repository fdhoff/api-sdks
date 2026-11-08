# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.notification.models.delivery_config import DeliveryConfig
from ebay_sell._runtime import ApiModel


class Destination(ApiModel):
    """Destination model."""

    delivery_config: Optional[DeliveryConfig] = Field(default=None, alias="deliveryConfig")
    destination_id: Optional[StrictStr] = Field(default=None, alias="destinationId")
    name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
