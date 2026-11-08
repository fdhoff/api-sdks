# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class UpdateListingInventoryRequestProductsInnerPropertyValuesInner(ApiModel):
    """UpdateListingInventoryRequestProductsInnerPropertyValuesInner model."""

    property_id: Annotated[int, Field(strict=True, ge=1)]
    value_ids: List[Annotated[int, Field(strict=True, ge=1)]]
    scale_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    property_name: Optional[StrictStr] = None
    values: List[StrictStr]
