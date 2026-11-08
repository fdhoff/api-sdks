# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.update_listing_inventory_request_products_inner_offerings_inner import (
    UpdateListingInventoryRequestProductsInnerOfferingsInner,
)
from etsy_seller.models.update_listing_inventory_request_products_inner_property_values_inner import (
    UpdateListingInventoryRequestProductsInnerPropertyValuesInner,
)
from etsy_seller._runtime import ApiModel


class UpdateListingInventoryRequestProductsInner(ApiModel):
    """UpdateListingInventoryRequestProductsInner model."""

    sku: Optional[StrictStr] = None
    property_values: Optional[List[UpdateListingInventoryRequestProductsInnerPropertyValuesInner]] = None
    offerings: List[UpdateListingInventoryRequestProductsInnerOfferingsInner]
