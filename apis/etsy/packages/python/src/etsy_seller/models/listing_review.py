# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ListingReview(ApiModel):
    """ListingReview model."""

    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    listing_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    rating: Optional[Annotated[int, Field(le=5, strict=True, ge=1)]] = None
    review: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    image_url_fullxfull: Optional[StrictStr] = None
    create_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    update_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
