# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_one_off_item_references import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItemReferences,
)
from mirakl_seller._runtime import ApiModel


class TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItem(ApiModel):
    """TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItem model."""

    description: Optional[StrictStr] = None
    operation_date: Optional[date] = None
    quantity: Optional[StrictInt] = None
    references: Optional[List[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItemReferences]] = None
    unit_price: Optional[float] = None
