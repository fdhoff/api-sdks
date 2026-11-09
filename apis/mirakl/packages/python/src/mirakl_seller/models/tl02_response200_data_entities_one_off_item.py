# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl02_response200_data_entities_one_off_item_references import (
    TL02Response200DataEntitiesOneOffItemReferences,
)
from mirakl_seller._runtime import ApiModel


class TL02Response200DataEntitiesOneOffItem(ApiModel):
    """TL02Response200DataEntitiesOneOffItem model."""

    description: Optional[StrictStr] = None
    operation_date: Optional[date] = None
    quantity: Optional[StrictInt] = None
    references: Optional[List[TL02Response200DataEntitiesOneOffItemReferences]] = None
    unit_price: Optional[float] = None
