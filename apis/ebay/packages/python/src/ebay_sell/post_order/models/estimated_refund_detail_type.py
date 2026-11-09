# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.estimated_refund_type import EstimatedRefundType
from ebay_sell._runtime import ApiModel


class EstimatedRefundDetailType(ApiModel):
    """EstimatedRefundDetailType model."""

    itemized_refund_details: Optional[List[EstimatedRefundType]] = Field(default=None, alias="itemizedRefundDetails")
    optional_refund_line_items: Optional[List[EstimatedRefundType]] = Field(
        default=None, alias="optionalRefundLineItems"
    )
