# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.return_address import ReturnAddress
from ebay_sell._runtime import ApiModel


class ContestPaymentDisputeRequest(ApiModel):
    """ContestPaymentDisputeRequest model."""

    note: Optional[StrictStr] = None
    return_address: Optional[ReturnAddress] = Field(default=None, alias="returnAddress")
    revision: Optional[StrictInt] = None
