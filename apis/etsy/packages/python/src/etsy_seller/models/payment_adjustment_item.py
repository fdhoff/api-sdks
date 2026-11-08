# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class PaymentAdjustmentItem(ApiModel):
    """PaymentAdjustmentItem model."""

    payment_adjustment_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    payment_adjustment_item_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    adjustment_type: Optional[StrictStr] = None
    amount: Optional[StrictInt] = 0
    shop_amount: Optional[StrictInt] = 0
    transaction_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    bill_payment_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
