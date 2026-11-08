# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Product(ApiModel):
    """Product model."""

    aspects: Optional[StrictStr] = None
    brand: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    ean: Optional[List[StrictStr]] = None
    epid: Optional[StrictStr] = None
    image_urls: Optional[List[StrictStr]] = Field(default=None, alias="imageUrls")
    isbn: Optional[List[StrictStr]] = None
    mpn: Optional[StrictStr] = None
    subtitle: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    upc: Optional[List[StrictStr]] = None
    video_ids: Optional[List[StrictStr]] = Field(default=None, alias="videoIds")
