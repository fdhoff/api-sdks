# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.tracking_info import TrackingInfo
from ebay_sell._runtime import ApiModel


class InfoFromBuyer(ApiModel):
    """InfoFromBuyer model."""

    content_on_hold: Optional[StrictBool] = Field(default=None, alias="contentOnHold")
    note: Optional[StrictStr] = None
    return_shipment_tracking: Optional[List[TrackingInfo]] = Field(default=None, alias="returnShipmentTracking")
