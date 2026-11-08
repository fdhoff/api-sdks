# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.listing_price import ListingPrice
from ebay_sell.feedback.models.order_line_item_attribute import OrderLineItemAttribute
from ebay_sell.feedback.models.transaction_period import TransactionPeriod
from ebay_sell._runtime import ApiModel


class OrderLineItemSummary(ApiModel):
    """OrderLineItemSummary model."""

    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    listing_price: Optional[ListingPrice] = Field(default=None, alias="listingPrice")
    listing_title: Optional[StrictStr] = Field(default=None, alias="listingTitle")
    order_line_item_attributes: Optional[List[OrderLineItemAttribute]] = Field(
        default=None, alias="orderLineItemAttributes"
    )
    order_line_item_id: Optional[StrictStr] = Field(default=None, alias="orderLineItemId")
    transaction_period: Optional[TransactionPeriod] = Field(default=None, alias="transactionPeriod")
