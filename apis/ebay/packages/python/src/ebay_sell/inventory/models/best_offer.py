# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.amount import Amount
from ebay_sell._runtime import ApiModel


class BestOffer(ApiModel):
    """BestOffer model."""

    auto_accept_price: Optional[Amount] = Field(default=None, alias="autoAcceptPrice")
    auto_decline_price: Optional[Amount] = Field(default=None, alias="autoDeclinePrice")
    best_offer_enabled: Optional[StrictBool] = Field(default=None, alias="bestOfferEnabled")
