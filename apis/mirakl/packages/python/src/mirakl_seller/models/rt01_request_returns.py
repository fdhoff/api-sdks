# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.rt01_request_returns_return_lines import RT01RequestReturnsReturnLines
from mirakl_seller._runtime import ApiModel


class RT01RequestReturns(ApiModel):
    """RT01RequestReturns model."""

    accepted: Optional[StrictBool] = None
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2000)]] = None
    label_url: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = None
    method_code: StrictStr
    order_commercial_id: StrictStr
    reason_code: Optional[StrictStr] = None
    return_lines: Annotated[List[RT01RequestReturnsReturnLines], Field(min_length=1, max_length=200)]
    rma: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = None
