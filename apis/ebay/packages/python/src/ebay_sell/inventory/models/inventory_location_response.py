# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.fulfillment_center_specifications import FulfillmentCenterSpecifications
from ebay_sell.inventory.models.location import Location
from ebay_sell.inventory.models.operating_hours import OperatingHours
from ebay_sell.inventory.models.special_hours import SpecialHours
from ebay_sell._runtime import ApiModel


class InventoryLocationResponse(ApiModel):
    """InventoryLocationResponse model."""

    location: Optional[Location] = None
    location_additional_information: Optional[StrictStr] = Field(default=None, alias="locationAdditionalInformation")
    location_instructions: Optional[StrictStr] = Field(default=None, alias="locationInstructions")
    location_types: Optional[List[StrictStr]] = Field(default=None, alias="locationTypes")
    location_web_url: Optional[StrictStr] = Field(default=None, alias="locationWebUrl")
    merchant_location_key: Optional[StrictStr] = Field(default=None, alias="merchantLocationKey")
    merchant_location_status: Optional[StrictStr] = Field(default=None, alias="merchantLocationStatus")
    name: Optional[StrictStr] = None
    operating_hours: Optional[List[OperatingHours]] = Field(default=None, alias="operatingHours")
    phone: Optional[StrictStr] = None
    special_hours: Optional[List[SpecialHours]] = Field(default=None, alias="specialHours")
    time_zone_id: Optional[StrictStr] = Field(default=None, alias="timeZoneId")
    fulfillment_center_specifications: Optional[FulfillmentCenterSpecifications] = Field(
        default=None, alias="fulfillmentCenterSpecifications"
    )
