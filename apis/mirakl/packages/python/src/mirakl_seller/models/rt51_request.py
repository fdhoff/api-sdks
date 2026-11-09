# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.rt51_request_return_labels import RT51RequestReturnLabels
from mirakl_seller._runtime import ApiModel


class RT51Request(ApiModel):
    """RT51Request model."""

    return_labels: Annotated[List[RT51RequestReturnLabels], Field(min_length=0, max_length=200)]
