# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class PostItemTransferCreateRequest(ApiModel):
    """PostItemTransferCreateRequest model."""

    shipper_name: StrictStr = Field(alias="shipperName")
    tracking_number: StrictStr = Field(alias="trackingNumber")
    action: Optional[StrictStr] = None
