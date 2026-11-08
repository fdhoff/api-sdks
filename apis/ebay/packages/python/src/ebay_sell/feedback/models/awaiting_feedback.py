# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.feedback_rating_template_type import FeedbackRatingTemplateType
from ebay_sell.feedback.models.listing_price import ListingPrice
from ebay_sell._runtime import ApiModel


class AwaitingFeedback(ApiModel):
    """AwaitingFeedback model."""

    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    listing_price: Optional[ListingPrice] = Field(default=None, alias="listingPrice")
    listing_title: Optional[StrictStr] = Field(default=None, alias="listingTitle")
    order_line_item_id: Optional[StrictStr] = Field(default=None, alias="orderLineItemId")
    rating_templates: Optional[List[FeedbackRatingTemplateType]] = Field(default=None, alias="ratingTemplates")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
