# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.seller_actions_to_release import SellerActionsToRelease
from ebay_sell._runtime import ApiModel


class PaymentHold(ApiModel):
    """PaymentHold model."""

    expected_release_date: Optional[StrictStr] = Field(default=None, alias="expectedReleaseDate")
    hold_amount: Optional[Amount] = Field(default=None, alias="holdAmount")
    hold_reason: Optional[StrictStr] = Field(default=None, alias="holdReason")
    hold_state: Optional[StrictStr] = Field(default=None, alias="holdState")
    release_date: Optional[StrictStr] = Field(default=None, alias="releaseDate")
    seller_actions_to_release: Optional[List[SellerActionsToRelease]] = Field(
        default=None, alias="sellerActionsToRelease"
    )
