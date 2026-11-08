# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.property_names_response_property_names import PropertyNamesResponsePropertyNames
from ebay_sell._runtime import ApiModel


class PropertyNamesResponseProperties(ApiModel):
    """PropertyNamesResponseProperties model."""

    dataset: Optional[StrictStr] = None
    property_names: Optional[List[PropertyNamesResponsePropertyNames]] = Field(default=None, alias="propertyNames")
