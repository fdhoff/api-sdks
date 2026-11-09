# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of54_response200_ext_file_structure_prices_context import (
    OF54Response200ExtFileStructurePricesContext,
)
from mirakl_seller.models.of54_response200_ext_file_structure_prices_volume_prices import (
    OF54Response200ExtFileStructurePricesVolumePrices,
)
from mirakl_seller._runtime import ApiModel


class OF54Response200ExtFileStructurePrices(ApiModel):
    """OF54Response200ExtFileStructurePrices model."""

    context: Optional[OF54Response200ExtFileStructurePricesContext] = None
    discount_end_date: Optional[StrictStr] = None
    discount_price: Optional[float] = None
    discount_start_date: Optional[StrictStr] = None
    origin_price: Optional[float] = None
    volume_prices: Optional[List[OF54Response200ExtFileStructurePricesVolumePrices]] = None
