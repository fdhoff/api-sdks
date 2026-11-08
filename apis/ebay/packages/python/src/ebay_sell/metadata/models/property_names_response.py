# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.property_names_response_properties import PropertyNamesResponseProperties
from ebay_sell._runtime import ApiModel


class PropertyNamesResponse(ApiModel):
    """PropertyNamesResponse model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    properties: Optional[List[PropertyNamesResponseProperties]] = None
