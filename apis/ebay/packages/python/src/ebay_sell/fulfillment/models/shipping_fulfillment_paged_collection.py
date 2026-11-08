# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.error import Error
from ebay_sell.fulfillment.models.shipping_fulfillment import ShippingFulfillment
from ebay_sell._runtime import ApiModel


class ShippingFulfillmentPagedCollection(ApiModel):
    """ShippingFulfillmentPagedCollection model."""

    fulfillments: Optional[List[ShippingFulfillment]] = None
    total: Optional[StrictInt] = None
    warnings: Optional[List[Error]] = None
