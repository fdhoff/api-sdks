# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or30_request_cancelations import OR30RequestCancelations
from mirakl_seller._runtime import ApiModel


class OR30Request(ApiModel):
    """OR30Request model."""

    cancelations: List[OR30RequestCancelations]
    order_tax_mode: Optional[StrictStr] = None
