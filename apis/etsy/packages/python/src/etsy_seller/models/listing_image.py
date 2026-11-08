# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ListingImage(ApiModel):
    """ListingImage model."""

    listing_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    listing_image_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    hex_code: Optional[StrictStr] = None
    red: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    green: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    blue: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    hue: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    saturation: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    brightness: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    is_black_and_white: Optional[StrictBool] = None
    creation_tsz: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    rank: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    url_75x75: Optional[StrictStr] = None
    url_170x135: Optional[StrictStr] = None
    url_570x_n: Optional[StrictStr] = Field(default=None, alias="url_570xN")
    url_fullxfull: Optional[StrictStr] = None
    full_height: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    full_width: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    alt_text: Optional[StrictStr] = None
