# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ProvisionalRefundType(ApiModel):
    """ProvisionalRefundType model."""

    refund_provided: Optional[StrictBool] = Field(default=None, alias="refundProvided")
    refund_reversed: Optional[StrictBool] = Field(default=None, alias="refundReversed")
