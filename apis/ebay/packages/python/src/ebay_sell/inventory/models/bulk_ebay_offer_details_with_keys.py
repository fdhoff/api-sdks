# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.ebay_offer_details_with_keys import EbayOfferDetailsWithKeys
from ebay_sell._runtime import ApiModel


class BulkEbayOfferDetailsWithKeys(ApiModel):
    """BulkEbayOfferDetailsWithKeys model."""

    requests: Optional[List[EbayOfferDetailsWithKeys]] = None
