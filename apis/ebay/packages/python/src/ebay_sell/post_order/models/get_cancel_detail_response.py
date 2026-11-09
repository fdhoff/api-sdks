# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.cancel_detail import CancelDetail
from ebay_sell._runtime import ApiModel


class GetCancelDetailResponse(ApiModel):
    """GetCancelDetailResponse model."""

    cancel_detail: Optional[CancelDetail] = Field(default=None, alias="cancelDetail")
