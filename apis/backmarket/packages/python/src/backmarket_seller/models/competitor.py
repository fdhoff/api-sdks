# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from backmarket_seller.models.market_code import MarketCode
from backmarket_seller.models.monetary_amount import MonetaryAmount
from backmarket_seller._runtime import ApiModel


class Competitor(ApiModel):
    """Competitor model."""

    is_winning: StrictBool
    listing_id: UUID
    min_price: Optional[MonetaryAmount]
    price: MonetaryAmount
    price_to_win: MonetaryAmount
    product_id: UUID
    winner_price: Optional[MonetaryAmount]
    market: MarketCode
