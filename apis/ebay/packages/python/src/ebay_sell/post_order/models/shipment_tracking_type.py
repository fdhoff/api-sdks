# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_address_type import ReturnAddressType
from ebay_sell.post_order.models.return_user_role_enum import ReturnUserRoleEnum
from ebay_sell.post_order.models.shipping_method_enum import ShippingMethodEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell.post_order.models.tracking_status_enum import TrackingStatusEnum
from ebay_sell._runtime import ApiModel


class ShipmentTrackingType(ApiModel):
    """ShipmentTrackingType model."""

    active: Optional[StrictBool] = None
    actual_delivery_date: Optional[Timestamp] = Field(default=None, alias="actualDeliveryDate")
    actual_ship_date: Optional[Timestamp] = Field(default=None, alias="actualShipDate")
    carrier_enum: Optional[StrictStr] = Field(default=None, alias="carrierEnum")
    carrier_id: Optional[StrictInt] = Field(default=None, alias="carrierId")
    carrier_name: Optional[StrictStr] = Field(default=None, alias="carrierName")
    carrier_used: Optional[StrictStr] = Field(default=None, alias="carrierUsed")
    delivery_date: Optional[Timestamp] = Field(default=None, alias="deliveryDate")
    delivery_status: Optional[TrackingStatusEnum] = Field(default=None, alias="deliveryStatus")
    destination_address: Optional[ReturnAddressType] = Field(default=None, alias="destinationAddress")
    error_code: Optional[StrictStr] = Field(default=None, alias="errorCode")
    label_available_until_date: Optional[StrictStr] = Field(default=None, alias="labelAvailableUntilDate")
    label_date: Optional[Timestamp] = Field(default=None, alias="labelDate")
    label_id: Optional[StrictStr] = Field(default=None, alias="labelId")
    label_print_expired: Optional[StrictBool] = Field(default=None, alias="labelPrintExpired")
    label_void_expired: Optional[StrictBool] = Field(default=None, alias="labelVoidExpired")
    mark_as_received: Optional[StrictBool] = Field(default=None, alias="markAsReceived")
    max_delivery_estimate: Optional[Timestamp] = Field(default=None, alias="maxDeliveryEstimate")
    min_delivery_estimate: Optional[Timestamp] = Field(default=None, alias="minDeliveryEstimate")
    origin_address: Optional[ReturnAddressType] = Field(default=None, alias="originAddress")
    ship_date: Optional[Timestamp] = Field(default=None, alias="shipDate")
    shipment_id: Optional[StrictStr] = Field(default=None, alias="shipmentId")
    shipped_by: Optional[ReturnUserRoleEnum] = Field(default=None, alias="shippedBy")
    shipping_method: Optional[ShippingMethodEnum] = Field(default=None, alias="shippingMethod")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
