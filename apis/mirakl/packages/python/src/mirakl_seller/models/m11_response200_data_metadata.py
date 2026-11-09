# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.m11_response200_data_metadata_last_sender import M11Response200DataMetadataLastSender
from mirakl_seller._runtime import ApiModel


class M11Response200DataMetadata(ApiModel):
    """M11Response200DataMetadata model."""

    last_message_date: datetime
    last_sender: M11Response200DataMetadataLastSender
    shop_reply_needed_since: datetime
    total_count: StrictInt
