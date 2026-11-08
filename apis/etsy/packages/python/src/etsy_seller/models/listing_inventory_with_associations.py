# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.listing_inventory_product import ListingInventoryProduct
from etsy_seller.models.shop_listing import ShopListing
from etsy_seller._runtime import ApiModel


class ListingInventoryWithAssociations(ApiModel):
    """ListingInventoryWithAssociations model."""

    products: Optional[List[ListingInventoryProduct]] = None
    price_on_property: Optional[List[StrictInt]] = None
    quantity_on_property: Optional[List[StrictInt]] = None
    sku_on_property: Optional[List[StrictInt]] = None
    readiness_state_on_property: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None
    listing: Optional[ShopListing] = None
