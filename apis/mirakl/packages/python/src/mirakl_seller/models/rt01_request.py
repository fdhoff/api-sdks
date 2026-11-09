# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.rt01_request_returns import RT01RequestReturns
from mirakl_seller._runtime import ApiModel


class RT01Request(ApiModel):
    """RT01Request model."""

    returns: Annotated[List[RT01RequestReturns], Field(min_length=1, max_length=200)]
