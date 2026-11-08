# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.property_filter_inner import PropertyFilterInner
from ebay_sell._runtime import ApiModel


class PropertyValuesRequest(ApiModel):
    """PropertyValuesRequest model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    property_filters: Optional[List[PropertyFilterInner]] = Field(default=None, alias="propertyFilters")
    property_name: Optional[StrictStr] = Field(default=None, alias="propertyName")
    sort_order: Optional[StrictStr] = Field(default=None, alias="sortOrder")
