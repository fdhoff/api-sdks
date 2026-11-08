# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.listing_inventory_product_offering import ListingInventoryProductOffering
from etsy_seller.models.listing_property_value import ListingPropertyValue
from etsy_seller._runtime import ApiModel


class ListingInventoryProduct(ApiModel):
    """ListingInventoryProduct model."""

    product_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    sku: Optional[StrictStr] = None
    is_deleted: Optional[StrictBool] = None
    offerings: Optional[List[ListingInventoryProductOffering]] = None
    property_values: Optional[List[ListingPropertyValue]] = None
