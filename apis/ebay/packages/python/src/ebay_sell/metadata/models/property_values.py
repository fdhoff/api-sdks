# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PropertyValues(ApiModel):
    """PropertyValues model."""

    property_name: Optional[StrictStr] = Field(default=None, alias="propertyName")
    property_value: Optional[StrictStr] = Field(default=None, alias="propertyValue")
