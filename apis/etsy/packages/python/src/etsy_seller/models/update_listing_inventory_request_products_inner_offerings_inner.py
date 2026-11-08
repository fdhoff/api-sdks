# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class UpdateListingInventoryRequestProductsInnerOfferingsInner(ApiModel):
    """UpdateListingInventoryRequestProductsInnerOfferingsInner model."""

    price: float
    quantity: StrictInt
    is_enabled: StrictBool
    readiness_state_id: Optional[Annotated[int, Field(strict=True, ge=1)]]
