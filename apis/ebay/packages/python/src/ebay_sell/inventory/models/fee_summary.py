# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.error import Error
from ebay_sell.inventory.models.fee import Fee
from ebay_sell._runtime import ApiModel


class FeeSummary(ApiModel):
    """FeeSummary model."""

    fees: Optional[List[Fee]] = None
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    warnings: Optional[List[Error]] = None
