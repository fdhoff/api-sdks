# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class PR01Response200PromotionsTriggers(ApiModel):
    """PR01Response200PromotionsTriggers model."""

    amount_purchased: Optional[float] = None
    quantity_purchased: Optional[StrictInt] = None
    same_item_purchased: Optional[StrictBool] = None
    type: StrictStr
