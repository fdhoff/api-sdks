# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.amount import Amount
from ebay_sell.account.models.shipping_service import ShippingService
from ebay_sell._runtime import ApiModel


class ShippingOption(ApiModel):
    """ShippingOption model."""

    cost_type: Optional[StrictStr] = Field(default=None, alias="costType")
    insurance_fee: Optional[Amount] = Field(default=None, alias="insuranceFee")
    insurance_offered: Optional[StrictBool] = Field(default=None, alias="insuranceOffered")
    option_type: Optional[StrictStr] = Field(default=None, alias="optionType")
    package_handling_cost: Optional[Amount] = Field(default=None, alias="packageHandlingCost")
    rate_table_id: Optional[StrictStr] = Field(default=None, alias="rateTableId")
    shipping_discount_profile_id: Optional[StrictStr] = Field(default=None, alias="shippingDiscountProfileId")
    shipping_promotion_offered: Optional[StrictBool] = Field(default=None, alias="shippingPromotionOffered")
    shipping_services: Optional[List[ShippingService]] = Field(default=None, alias="shippingServices")
