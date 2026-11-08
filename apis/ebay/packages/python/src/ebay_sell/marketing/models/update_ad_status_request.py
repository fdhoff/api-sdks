# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class UpdateAdStatusRequest(ApiModel):
    """UpdateAdStatusRequest model."""

    ad_id: Optional[StrictStr] = Field(default=None, alias="adId")
    ad_status: Optional[StrictStr] = Field(default=None, alias="adStatus")
