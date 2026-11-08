# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.ebay_tax_reference import EbayTaxReference
from ebay_sell._runtime import ApiModel


class EbayCollectAndRemitTax(ApiModel):
    """EbayCollectAndRemitTax model."""

    amount: Optional[Amount] = None
    ebay_reference: Optional[EbayTaxReference] = Field(default=None, alias="ebayReference")
    tax_type: Optional[StrictStr] = Field(default=None, alias="taxType")
    collection_method: Optional[StrictStr] = Field(default=None, alias="collectionMethod")
