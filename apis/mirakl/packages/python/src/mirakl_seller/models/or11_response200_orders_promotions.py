# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or11_response200_orders_promotions_applied_promotions import (
    OR11Response200OrdersPromotionsAppliedPromotions,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersPromotions(ApiModel):
    """OR11Response200OrdersPromotions model."""

    applied_promotions: List[OR11Response200OrdersPromotionsAppliedPromotions]
    total_deduced_amount: float
