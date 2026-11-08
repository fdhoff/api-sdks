# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.shop_receipt_transaction import ShopReceiptTransaction
from etsy_seller._runtime import ApiModel


class ShopReceiptTransactions(ApiModel):
    """ShopReceiptTransactions model."""

    count: Optional[StrictInt] = None
    results: Optional[List[ShopReceiptTransaction]] = None
