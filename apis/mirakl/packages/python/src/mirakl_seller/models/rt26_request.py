# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.rt26_request_returns import RT26RequestReturns
from mirakl_seller._runtime import ApiModel


class RT26Request(ApiModel):
    """RT26Request model."""

    returns: Annotated[List[RT26RequestReturns], Field(min_length=1, max_length=100)]
