# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller.models.pickup_info import PickupInfo
from backmarket_seller._runtime import ApiModel


class Delivery(ApiModel):
    """Delivery model."""

    order: StrictInt
    shipment_id: StrictInt = Field(alias="shipmentId")
    carrier_id: StrictInt = Field(alias="carrierId")
    orderlines: List[StrictInt]
    reference_number: StrictStr = Field(alias="referenceNumber")
    tracking_number: StrictStr = Field(alias="trackingNumber")
    tracking_url: StrictStr = Field(alias="trackingUrl")
    carrier_name: StrictStr = Field(alias="carrierName")
    hub_scanned: StrictBool = Field(alias="hubScanned")
    invoiced_currency: StrictStr = Field(alias="invoicedCurrency")
    invoiced_price: StrictInt = Field(alias="invoicedPrice")
    date_pickup: datetime = Field(alias="datePickup")
    date_creation: datetime = Field(alias="dateCreation")
    date_delivery: datetime = Field(alias="dateDelivery")
    label_url: StrictStr = Field(alias="labelUrl")
    type: StrictStr
    pickup_info: PickupInfo = Field(alias="pickupInfo")
