# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class PostRefundCreateRequest(ApiModel):
    """PostRefundCreateRequest model."""

    amount: Optional[float] = None
    orderline_pk: Optional[StrictInt] = None
    refund_type: Optional[StrictInt] = None
