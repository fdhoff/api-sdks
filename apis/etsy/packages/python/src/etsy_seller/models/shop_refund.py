# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller._runtime import ApiModel


class ShopRefund(ApiModel):
    """ShopRefund model."""

    amount: Optional[Money] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    reason: Optional[StrictStr] = None
    note_from_issuer: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
