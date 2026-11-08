# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.package_limits import PackageLimits
from ebay_sell._runtime import ApiModel


class ShippingService(ApiModel):
    """ShippingService model."""

    description: Optional[StrictStr] = None
    international_service: Optional[StrictBool] = Field(default=None, alias="internationalService")
    max_shipping_time: Optional[StrictInt] = Field(default=None, alias="maxShippingTime")
    min_shipping_time: Optional[StrictInt] = Field(default=None, alias="minShippingTime")
    package_limits: Optional[PackageLimits] = Field(default=None, alias="packageLimits")
    shipping_carrier: Optional[StrictStr] = Field(default=None, alias="shippingCarrier")
    shipping_category: Optional[StrictStr] = Field(default=None, alias="shippingCategory")
    shipping_cost_types: Optional[List[StrictStr]] = Field(default=None, alias="shippingCostTypes")
    shipping_service: Optional[StrictStr] = Field(default=None, alias="shippingService")
    valid_for_selling_flow: Optional[StrictBool] = Field(default=None, alias="validForSellingFlow")
