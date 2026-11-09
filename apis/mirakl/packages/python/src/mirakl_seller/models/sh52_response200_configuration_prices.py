# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.sh52_response200_configuration_prices_ranges import SH52Response200ConfigurationPricesRanges
from mirakl_seller._runtime import ApiModel


class SH52Response200ConfigurationPrices(ApiModel):
    """SH52Response200ConfigurationPrices model."""

    additional_price: Optional[float] = None
    free_shipping_threshold: Optional[float] = None
    initial_price: Optional[float] = None
    ranges: Optional[List[SH52Response200ConfigurationPricesRanges]] = None
    type: StrictStr
