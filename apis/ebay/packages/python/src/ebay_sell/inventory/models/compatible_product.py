# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.name_value_list import NameValueList
from ebay_sell.inventory.models.product_family_properties import ProductFamilyProperties
from ebay_sell.inventory.models.product_identifier import ProductIdentifier
from ebay_sell._runtime import ApiModel


class CompatibleProduct(ApiModel):
    """CompatibleProduct model."""

    compatibility_properties: Optional[List[NameValueList]] = Field(default=None, alias="compatibilityProperties")
    notes: Optional[StrictStr] = None
    product_family_properties: Optional[ProductFamilyProperties] = Field(default=None, alias="productFamilyProperties")
    product_identifier: Optional[ProductIdentifier] = Field(default=None, alias="productIdentifier")
