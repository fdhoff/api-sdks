# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.price_quantity_response import PriceQuantityResponse
from ebay_sell._runtime import ApiModel


class BulkPriceQuantityResponse(ApiModel):
    """BulkPriceQuantityResponse model."""

    responses: Optional[List[PriceQuantityResponse]] = None
