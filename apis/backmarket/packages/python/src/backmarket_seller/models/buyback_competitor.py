# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from backmarket_seller.models.market_code import MarketCode
from backmarket_seller.models.monetary_amount import MonetaryAmount
from backmarket_seller._runtime import ApiModel


class BuybackCompetitor(ApiModel):
    """BuybackCompetitor model."""

    listing_id: UUID
    product_id: UUID
    market: MarketCode
    price: Optional[MonetaryAmount] = None
    price_to_win: MonetaryAmount
    is_winning: StrictBool
    winner_price: Optional[MonetaryAmount]
