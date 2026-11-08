# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.ebay_offer_details_with_all import EbayOfferDetailsWithAll
from ebay_sell._runtime import ApiModel


class Offers(ApiModel):
    """Offers model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offers: Optional[List[EbayOfferDetailsWithAll]] = None
    prev: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    total: Optional[StrictInt] = None
