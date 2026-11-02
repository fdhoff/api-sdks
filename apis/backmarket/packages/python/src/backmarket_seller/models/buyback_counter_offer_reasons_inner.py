# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller.models.buyback_counter_offer_reason_category import BuybackCounterOfferReasonCategory
from backmarket_seller.models.buyback_counter_offer_reasons_inner_reasons_inner import (
    BuybackCounterOfferReasonsInnerReasonsInner,
)
from backmarket_seller._runtime import ApiModel


class BuybackCounterOfferReasonsInner(ApiModel):
    """BuybackCounterOfferReasonsInner model."""

    id: BuybackCounterOfferReasonCategory
    label: StrictStr
    reasons: List[BuybackCounterOfferReasonsInnerReasonsInner]
