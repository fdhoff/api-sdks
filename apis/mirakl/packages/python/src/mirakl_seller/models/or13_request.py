# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR13Request(ApiModel):
    """OR13Request model."""

    channel_codes: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    end_date: Optional[datetime] = None
    end_update_date: Optional[datetime] = None
    fulfillment_center_codes: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=100)]] = None
    items_per_chunk: Optional[Annotated[int, Field(le=1000000, strict=True, ge=10000)]] = 1000000
    megabytes_per_chunk: Optional[Annotated[int, Field(le=1024, strict=True, ge=10)]] = 512
    only_null_channel: Optional[StrictBool] = False
    order_state_codes: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    order_tax_mode: Optional[StrictStr] = None
    start_date: Optional[datetime] = None
    start_update_date: Optional[datetime] = None
