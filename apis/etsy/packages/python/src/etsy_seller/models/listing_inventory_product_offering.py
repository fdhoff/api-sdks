# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller._runtime import ApiModel


class ListingInventoryProductOffering(ApiModel):
    """ListingInventoryProductOffering model."""

    offering_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    quantity: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    is_enabled: Optional[StrictBool] = None
    is_deleted: Optional[StrictBool] = None
    price: Optional[Money] = None
    readiness_state_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
