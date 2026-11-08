# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.listing_property_value import ListingPropertyValue
from etsy_seller.models.money import Money
from etsy_seller.models.transaction_variations import TransactionVariations
from etsy_seller._runtime import ApiModel


class ShopReceiptTransaction(ApiModel):
    """ShopReceiptTransaction model."""

    transaction_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    seller_user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    buyer_user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    create_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    paid_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    shipped_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    quantity: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    listing_image_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    receipt_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    is_digital: Optional[StrictBool] = None
    file_data: Optional[StrictStr] = None
    listing_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    transaction_type: Optional[StrictStr] = None
    product_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    sku: Optional[StrictStr] = None
    price: Optional[Money] = None
    shipping_cost: Optional[Money] = None
    variations: Optional[List[TransactionVariations]] = None
    product_data: Optional[List[ListingPropertyValue]] = None
    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    min_processing_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    max_processing_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    shipping_method: Optional[StrictStr] = None
    shipping_upgrade: Optional[StrictStr] = None
    expected_ship_date: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    buyer_coupon: Optional[float] = 0
    shop_coupon: Optional[float] = 0
