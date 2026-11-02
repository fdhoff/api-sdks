# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller._runtime import ApiModel


class ReturnShipment(ApiModel):
    """ReturnShipment model."""

    order_id: StrictInt = Field(alias="orderId")
    orderline_id: StrictInt = Field(alias="orderlineId")
    shipment_id: StrictInt = Field(alias="shipmentId")
    carrier_id: StrictInt = Field(alias="carrierId")
    carrier_name: StrictStr = Field(alias="carrierName")
    date_creation: datetime = Field(alias="dateCreation")
    reference_number: StrictStr = Field(alias="referenceNumber")
    tracking_number: StrictStr = Field(alias="trackingNumber")
    tracking_url: StrictStr = Field(alias="trackingUrl")
    hub_scanned: StrictBool = Field(alias="hubScanned")
    date_pickup: datetime = Field(alias="datePickup")
    date_delivery: datetime = Field(alias="dateDelivery")
    label: StrictStr
    invoiced_price: StrictInt = Field(alias="invoicedPrice")
    invoiced_currency: StrictStr = Field(alias="invoicedCurrency")
    type: StrictStr
