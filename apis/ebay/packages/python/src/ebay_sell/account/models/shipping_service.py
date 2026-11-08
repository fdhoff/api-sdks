# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.amount import Amount
from ebay_sell.account.models.region_set import RegionSet
from ebay_sell._runtime import ApiModel


class ShippingService(ApiModel):
    """ShippingService model."""

    additional_shipping_cost: Optional[Amount] = Field(default=None, alias="additionalShippingCost")
    buyer_responsible_for_pickup: Optional[StrictBool] = Field(default=None, alias="buyerResponsibleForPickup")
    buyer_responsible_for_shipping: Optional[StrictBool] = Field(default=None, alias="buyerResponsibleForShipping")
    free_shipping: Optional[StrictBool] = Field(default=None, alias="freeShipping")
    shipping_carrier_code: Optional[StrictStr] = Field(default=None, alias="shippingCarrierCode")
    shipping_cost: Optional[Amount] = Field(default=None, alias="shippingCost")
    shipping_service_code: Optional[StrictStr] = Field(default=None, alias="shippingServiceCode")
    ship_to_locations: Optional[RegionSet] = Field(default=None, alias="shipToLocations")
    sort_order: Optional[StrictInt] = Field(default=None, alias="sortOrder")
    surcharge: Optional[Amount] = None
