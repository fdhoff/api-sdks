# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.m10_response200_metadata_last_sender import M10Response200MetadataLastSender
from mirakl_seller._runtime import ApiModel


class M10Response200Metadata(ApiModel):
    """M10Response200Metadata model."""

    last_message_date: datetime
    last_sender: M10Response200MetadataLastSender
    shop_reply_needed_since: datetime
    total_count: StrictInt
