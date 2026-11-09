# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_shipping_cost_detail_type import ReturnShippingCostDetailType
from ebay_sell.post_order.models.return_user_role_enum import ReturnUserRoleEnum
from ebay_sell.post_order.models.shipment_tracking_type import ShipmentTrackingType
from ebay_sell._runtime import ApiModel


class ShipmentType(ApiModel):
    """ShipmentType model."""

    all_shipment_trackings: Optional[List[ShipmentTrackingType]] = Field(default=None, alias="allShipmentTrackings")
    payee: Optional[ReturnUserRoleEnum] = None
    shipment_tracking: Optional[ShipmentTrackingType] = Field(default=None, alias="shipmentTracking")
    shipping_label_cost: Optional[ReturnShippingCostDetailType] = Field(default=None, alias="shippingLabelCost")
