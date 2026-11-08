# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.rate import Rate
from ebay_sell._runtime import ApiModel


class RateTableDetails(ApiModel):
    """RateTableDetails model."""

    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    rates: Optional[List[Rate]] = None
    rate_table_basis: Optional[StrictStr] = Field(default=None, alias="rateTableBasis")
    rate_table_id: Optional[StrictStr] = Field(default=None, alias="rateTableId")
    shipping_option_type: Optional[StrictStr] = Field(default=None, alias="shippingOptionType")
