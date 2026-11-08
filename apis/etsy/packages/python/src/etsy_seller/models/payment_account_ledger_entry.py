# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.payment_adjustment import PaymentAdjustment
from etsy_seller._runtime import ApiModel


class PaymentAccountLedgerEntry(ApiModel):
    """PaymentAccountLedgerEntry model."""

    entry_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    ledger_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    sequence_number: Optional[StrictInt] = None
    amount: Optional[StrictInt] = None
    currency: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    balance: Optional[StrictInt] = None
    create_date: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    ledger_type: Optional[StrictStr] = None
    reference_type: Optional[StrictStr] = None
    reference_id: Optional[StrictStr] = None
    parent_entry_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    payment_adjustments: Optional[List[PaymentAdjustment]] = None
