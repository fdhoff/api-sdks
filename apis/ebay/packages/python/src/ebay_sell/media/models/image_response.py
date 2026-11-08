# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ImageResponse(ApiModel):
    """ImageResponse model."""

    expiration_date: Optional[StrictStr] = Field(default=None, alias="expirationDate")
    image_url: Optional[StrictStr] = Field(default=None, alias="imageUrl")
    max_dimension_image_url: Optional[StrictStr] = Field(default=None, alias="maxDimensionImageUrl")
