# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.fee_jurisdiction import FeeJurisdiction
from ebay_sell._runtime import ApiModel


class Fee(ApiModel):
    """Fee model."""

    amount: Optional[Amount] = None
    fee_jurisdiction: Optional[FeeJurisdiction] = Field(default=None, alias="feeJurisdiction")
    fee_memo: Optional[StrictStr] = Field(default=None, alias="feeMemo")
    fee_type: Optional[StrictStr] = Field(default=None, alias="feeType")
