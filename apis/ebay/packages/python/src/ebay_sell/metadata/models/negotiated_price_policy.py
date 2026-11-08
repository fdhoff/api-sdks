# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class NegotiatedPricePolicy(ApiModel):
    """NegotiatedPricePolicy model."""

    best_offer_auto_accept_enabled: Optional[StrictBool] = Field(default=None, alias="bestOfferAutoAcceptEnabled")
    best_offer_auto_decline_enabled: Optional[StrictBool] = Field(default=None, alias="bestOfferAutoDeclineEnabled")
    best_offer_counter_enabled: Optional[StrictBool] = Field(default=None, alias="bestOfferCounterEnabled")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
