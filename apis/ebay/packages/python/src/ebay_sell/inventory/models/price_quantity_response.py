# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.error import Error
from ebay_sell._runtime import ApiModel


class PriceQuantityResponse(ApiModel):
    """PriceQuantityResponse model."""

    errors: Optional[List[Error]] = None
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerId")
    sku: Optional[StrictStr] = None
    status_code: Optional[StrictInt] = Field(default=None, alias="statusCode")
    warnings: Optional[List[Error]] = None
