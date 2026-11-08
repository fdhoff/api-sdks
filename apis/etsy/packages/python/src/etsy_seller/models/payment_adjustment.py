# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.payment_adjustment_item import PaymentAdjustmentItem
from etsy_seller._runtime import ApiModel


class PaymentAdjustment(ApiModel):
    """PaymentAdjustment model."""

    payment_adjustment_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    payment_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    status: Optional[StrictStr] = None
    is_success: Optional[StrictBool] = None
    user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    reason_code: Optional[StrictStr] = None
    total_adjustment_amount: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    shop_total_adjustment_amount: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    buyer_total_adjustment_amount: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    total_fee_adjustment_amount: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    create_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    update_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    payment_adjustment_items: Optional[List[PaymentAdjustmentItem]] = None
