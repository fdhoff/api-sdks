# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.amount import Amount
from ebay_sell._runtime import ApiModel


class ShippingPolicy(ApiModel):
    """ShippingPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    global_shipping_enabled: Optional[StrictBool] = Field(default=None, alias="globalShippingEnabled")
    group1_max_flat_shipping_cost: Optional[Amount] = Field(default=None, alias="group1MaxFlatShippingCost")
    group2_max_flat_shipping_cost: Optional[Amount] = Field(default=None, alias="group2MaxFlatShippingCost")
    group3_max_flat_shipping_cost: Optional[Amount] = Field(default=None, alias="group3MaxFlatShippingCost")
    handling_time_enabled: Optional[StrictBool] = Field(default=None, alias="handlingTimeEnabled")
    max_flat_shipping_cost: Optional[Amount] = Field(default=None, alias="maxFlatShippingCost")
    shipping_terms_required: Optional[StrictBool] = Field(default=None, alias="shippingTermsRequired")
