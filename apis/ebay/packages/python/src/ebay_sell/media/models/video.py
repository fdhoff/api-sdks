# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.media.models.image import Image
from ebay_sell.media.models.moderation import Moderation
from ebay_sell.media.models.play import Play
from ebay_sell._runtime import ApiModel


class Video(ApiModel):
    """Video model."""

    classification: Optional[List[StrictStr]] = None
    description: Optional[StrictStr] = None
    expiration_date: Optional[StrictStr] = Field(default=None, alias="expirationDate")
    moderation: Optional[Moderation] = None
    play_lists: Optional[List[Play]] = Field(default=None, alias="playLists")
    size: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    status_message: Optional[StrictStr] = Field(default=None, alias="statusMessage")
    thumbnail: Optional[Image] = None
    title: Optional[StrictStr] = None
    video_id: Optional[StrictStr] = Field(default=None, alias="videoId")
