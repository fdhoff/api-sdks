# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.recommendation.models.listing_recommendation import ListingRecommendation
from ebay_sell._runtime import ApiModel


class PagedListingRecommendationCollection(ApiModel):
    """PagedListingRecommendationCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    listing_recommendations: Optional[List[ListingRecommendation]] = Field(default=None, alias="listingRecommendations")
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
