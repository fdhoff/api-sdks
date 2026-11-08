# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.shop_listing_file import ShopListingFile
from etsy_seller._runtime import ApiModel


class ShopListingFiles(ApiModel):
    """ShopListingFiles model."""

    count: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    results: Optional[List[ShopListingFile]] = None
