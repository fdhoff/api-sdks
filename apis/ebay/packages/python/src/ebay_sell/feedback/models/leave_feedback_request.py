# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.image import Image
from ebay_sell.feedback.models.seller_rating import SellerRating
from ebay_sell._runtime import ApiModel


class LeaveFeedbackRequest(ApiModel):
    """LeaveFeedbackRequest model."""

    comment_text: Optional[StrictStr] = Field(default=None, alias="commentText")
    comment_type: Optional[StrictStr] = Field(default=None, alias="commentType")
    images: Optional[List[Image]] = None
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    order_line_item_id: Optional[StrictStr] = Field(default=None, alias="orderLineItemId")
    seller_ratings: Optional[List[SellerRating]] = Field(default=None, alias="sellerRatings")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
