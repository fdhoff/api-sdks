# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.name_value_pair import NameValuePair
from ebay_sell.fulfillment.models.tracking_info import TrackingInfo
from ebay_sell._runtime import ApiModel


class LinkedOrderLineItem(ApiModel):
    """LinkedOrderLineItem model."""

    line_item_aspects: Optional[List[NameValuePair]] = Field(default=None, alias="lineItemAspects")
    line_item_id: Optional[StrictStr] = Field(default=None, alias="lineItemId")
    max_estimated_delivery_date: Optional[StrictStr] = Field(default=None, alias="maxEstimatedDeliveryDate")
    min_estimated_delivery_date: Optional[StrictStr] = Field(default=None, alias="minEstimatedDeliveryDate")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    seller_id: Optional[StrictStr] = Field(default=None, alias="sellerId")
    shipments: Optional[List[TrackingInfo]] = None
    title: Optional[StrictStr] = None
