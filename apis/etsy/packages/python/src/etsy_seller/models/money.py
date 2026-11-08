# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class Money(ApiModel):
    """Money model."""

    amount: Optional[StrictInt] = None
    divisor: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    currency_code: Optional[StrictStr] = None
