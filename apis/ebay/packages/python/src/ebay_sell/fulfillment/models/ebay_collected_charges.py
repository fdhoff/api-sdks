# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.charge import Charge
from ebay_sell._runtime import ApiModel


class EbayCollectedCharges(ApiModel):
    """EbayCollectedCharges model."""

    ebay_shipping: Optional[Amount] = Field(default=None, alias="ebayShipping")
    charges: Optional[List[Charge]] = None
