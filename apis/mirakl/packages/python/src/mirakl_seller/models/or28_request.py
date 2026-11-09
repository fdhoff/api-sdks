# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or28_request_refunds import OR28RequestRefunds
from mirakl_seller._runtime import ApiModel


class OR28Request(ApiModel):
    """OR28Request model."""

    order_tax_mode: Optional[StrictStr] = None
    refunds: List[OR28RequestRefunds]
