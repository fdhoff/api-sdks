# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.compatibility_property_value import CompatibilityPropertyValue
from ebay_sell._runtime import ApiModel


class GetCompatibilityPropertyValuesResponse(ApiModel):
    """GetCompatibilityPropertyValuesResponse model."""

    compatibility_property_values: Optional[List[CompatibilityPropertyValue]] = Field(
        default=None, alias="compatibilityPropertyValues"
    )
