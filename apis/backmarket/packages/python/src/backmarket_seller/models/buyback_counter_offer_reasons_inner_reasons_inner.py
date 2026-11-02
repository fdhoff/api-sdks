# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class BuybackCounterOfferReasonsInnerReasonsInner(ApiModel):
    """BuybackCounterOfferReasonsInnerReasonsInner model."""

    id: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
