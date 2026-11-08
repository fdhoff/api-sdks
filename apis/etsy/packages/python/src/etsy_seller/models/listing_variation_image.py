# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ListingVariationImage(ApiModel):
    """ListingVariationImage model."""

    property_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    value_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    value: Optional[StrictStr] = None
    image_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
