# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.buyback_order import BuybackOrder
from backmarket_seller._runtime import ApiModel


class BuybackOrderPage(ApiModel):
    """BuybackOrderPage model."""

    count: StrictInt
    next: Optional[StrictStr]
    previous: Optional[StrictStr]
    results: Optional[List[BuybackOrder]] = None
