# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OF52Request(ApiModel):
    """OF52Request model."""

    channel_codes: Optional[List[StrictStr]] = None
    export_type: Optional[StrictStr] = None
    include_fields: Optional[List[StrictStr]] = None
    include_inactive_offers: Optional[StrictBool] = False
    items_per_chunk: Optional[Annotated[int, Field(le=1000000, strict=True, ge=10000)]] = None
    last_request_date: Optional[datetime] = None
    megabytes_per_chunk: Optional[Annotated[int, Field(le=1000, strict=True, ge=10)]] = None
    ongoing_discount_campaign_identifiers: Optional[List[StrictStr]] = None
    rename_fields: Optional[Dict[str, StrictStr]] = None
    shipping_zones: Optional[List[StrictStr]] = None
