# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or28_response200_refunds import OR28Response200Refunds
from mirakl_seller._runtime import ApiModel


class OR28Response200(ApiModel):
    """OR28Response200 model."""

    order_tax_mode: StrictStr
    refunds: List[OR28Response200Refunds]
