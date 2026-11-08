# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ListingVideo(ApiModel):
    """ListingVideo model."""

    video_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    height: Optional[StrictInt] = None
    width: Optional[StrictInt] = None
    thumbnail_url: Optional[StrictStr] = None
    video_url: Optional[StrictStr] = None
    video_state: Optional[StrictStr] = "active"
