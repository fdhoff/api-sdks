# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PackageLimits(ApiModel):
    """PackageLimits model."""

    dimension_unit: Optional[StrictStr] = Field(default=None, alias="dimensionUnit")
    max_girth: Optional[float] = Field(default=None, alias="maxGirth")
    max_height: Optional[float] = Field(default=None, alias="maxHeight")
    max_length: Optional[float] = Field(default=None, alias="maxLength")
    max_weight: Optional[float] = Field(default=None, alias="maxWeight")
    max_width: Optional[float] = Field(default=None, alias="maxWidth")
    min_girth: Optional[float] = Field(default=None, alias="minGirth")
    min_height: Optional[float] = Field(default=None, alias="minHeight")
    min_length: Optional[float] = Field(default=None, alias="minLength")
    min_weight: Optional[float] = Field(default=None, alias="minWeight")
    min_width: Optional[float] = Field(default=None, alias="minWidth")
    weight_unit: Optional[StrictStr] = Field(default=None, alias="weightUnit")
