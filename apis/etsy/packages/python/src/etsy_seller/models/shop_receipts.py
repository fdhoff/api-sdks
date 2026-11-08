# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.shop_receipt import ShopReceipt
from etsy_seller._runtime import ApiModel


class ShopReceipts(ApiModel):
    """ShopReceipts model."""

    count: Optional[StrictInt] = None
    results: Optional[List[ShopReceipt]] = None
