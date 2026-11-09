# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.rt27_request_returns import RT27RequestReturns
from mirakl_seller._runtime import ApiModel


class RT27Request(ApiModel):
    """RT27Request model."""

    returns: Annotated[List[RT27RequestReturns], Field(min_length=1, max_length=100)]
