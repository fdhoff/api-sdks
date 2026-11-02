# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.monetary_amount import MonetaryAmount
from backmarket_seller._runtime import ApiModel


class BuybackListingUpdate(ApiModel):
    """BuybackListingUpdate model."""

    prices: Optional[Dict[str, MonetaryAmount]] = None
