# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.voluntary_refund_result import VoluntaryRefundResult
from ebay_sell._runtime import ApiModel


class VoluntaryRefundResponse(ApiModel):
    """VoluntaryRefundResponse model."""

    refund_result: Optional[VoluntaryRefundResult] = Field(default=None, alias="refundResult")
