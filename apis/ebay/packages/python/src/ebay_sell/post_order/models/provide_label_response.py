# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ProvideLabelResponse(ApiModel):
    """ProvideLabelResponse model."""

    label_data: Optional[StrictStr] = Field(default=None, alias="labelData")
    label_id: Optional[StrictStr] = Field(default=None, alias="labelId")
    label_url: Optional[StrictStr] = Field(default=None, alias="labelURL")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
