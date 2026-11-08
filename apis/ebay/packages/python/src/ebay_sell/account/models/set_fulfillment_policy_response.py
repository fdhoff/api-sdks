# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.category_type import CategoryType
from ebay_sell.account.models.error import Error
from ebay_sell.account.models.region_set import RegionSet
from ebay_sell.account.models.shipping_option import ShippingOption
from ebay_sell.account.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class SetFulfillmentPolicyResponse(ApiModel):
    """SetFulfillmentPolicyResponse model."""

    category_types: Optional[List[CategoryType]] = Field(default=None, alias="categoryTypes")
    description: Optional[StrictStr] = None
    freight_shipping: Optional[StrictBool] = Field(default=None, alias="freightShipping")
    fulfillment_policy_id: Optional[StrictStr] = Field(default=None, alias="fulfillmentPolicyId")
    global_shipping: Optional[StrictBool] = Field(default=None, alias="globalShipping")
    handling_time: Optional[TimeDuration] = Field(default=None, alias="handlingTime")
    local_pickup: Optional[StrictBool] = Field(default=None, alias="localPickup")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    pickup_drop_off: Optional[StrictBool] = Field(default=None, alias="pickupDropOff")
    shipping_options: Optional[List[ShippingOption]] = Field(default=None, alias="shippingOptions")
    ship_to_locations: Optional[RegionSet] = Field(default=None, alias="shipToLocations")
    warnings: Optional[List[Error]] = None
