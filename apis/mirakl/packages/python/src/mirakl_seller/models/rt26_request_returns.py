# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.rt26_request_returns_return_lines import RT26RequestReturnsReturnLines
from mirakl_seller._runtime import ApiModel


class RT26RequestReturns(ApiModel):
    """RT26RequestReturns model."""

    id: StrictStr
    return_lines: Annotated[List[RT26RequestReturnsReturnLines], Field(min_length=1, max_length=200)]
