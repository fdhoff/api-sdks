# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.availability_with_all import AvailabilityWithAll
from ebay_sell.inventory.models.condition_descriptor import ConditionDescriptor
from ebay_sell.inventory.models.package_weight_and_size import PackageWeightAndSize
from ebay_sell.inventory.models.product import Product
from ebay_sell._runtime import ApiModel


class InventoryItemWithSkuLocaleGroupKeys(ApiModel):
    """InventoryItemWithSkuLocaleGroupKeys model."""

    availability: Optional[AvailabilityWithAll] = None
    condition: Optional[StrictStr] = None
    condition_description: Optional[StrictStr] = Field(default=None, alias="conditionDescription")
    condition_descriptors: Optional[List[ConditionDescriptor]] = Field(default=None, alias="conditionDescriptors")
    inventory_item_group_keys: Optional[List[StrictStr]] = Field(default=None, alias="inventoryItemGroupKeys")
    locale: Optional[StrictStr] = None
    package_weight_and_size: Optional[PackageWeightAndSize] = Field(default=None, alias="packageWeightAndSize")
    product: Optional[Product] = None
    sku: Optional[StrictStr] = None
