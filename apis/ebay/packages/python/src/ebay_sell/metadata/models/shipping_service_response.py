# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.shipping_service import ShippingService
from ebay_sell._runtime import ApiModel


class ShippingServiceResponse(ApiModel):
    """ShippingServiceResponse model."""

    shipping_services: Optional[List[ShippingService]] = Field(default=None, alias="shippingServices")
