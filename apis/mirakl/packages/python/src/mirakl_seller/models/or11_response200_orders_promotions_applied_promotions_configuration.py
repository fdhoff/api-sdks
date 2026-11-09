# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersPromotionsAppliedPromotionsConfiguration(ApiModel):
    """OR11Response200OrdersPromotionsAppliedPromotionsConfiguration model."""

    amount_off: Optional[float] = None
    free_items_quantity: Optional[StrictInt] = None
    internal_description: StrictStr
    percentage_off: Optional[float] = None
    reduced_unit_price: Optional[float] = None
    type: StrictStr
