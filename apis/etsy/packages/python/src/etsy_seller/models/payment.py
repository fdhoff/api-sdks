# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller.models.payment_adjustment import PaymentAdjustment
from etsy_seller._runtime import ApiModel


class Payment(ApiModel):
    """Payment model."""

    payment_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    buyer_user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    receipt_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    amount_gross: Optional[Money] = None
    amount_fees: Optional[Money] = None
    amount_net: Optional[Money] = None
    posted_gross: Optional[Money] = None
    posted_fees: Optional[Money] = None
    posted_net: Optional[Money] = None
    adjusted_gross: Optional[Money] = None
    adjusted_fees: Optional[Money] = None
    adjusted_net: Optional[Money] = None
    currency: Optional[StrictStr] = None
    shop_currency: Optional[StrictStr] = None
    buyer_currency: Optional[StrictStr] = None
    shipping_user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shipping_address_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    billing_address_id: Optional[Annotated[int, Field(le=9223372036854776000, strict=True, ge=0)]] = None
    status: Optional[StrictStr] = None
    shipped_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    create_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    update_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    payment_adjustments: Optional[List[PaymentAdjustment]] = None
