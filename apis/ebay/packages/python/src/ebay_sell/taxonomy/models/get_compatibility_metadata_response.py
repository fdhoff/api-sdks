# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.compatibility_property import CompatibilityProperty
from ebay_sell._runtime import ApiModel


class GetCompatibilityMetadataResponse(ApiModel):
    """GetCompatibilityMetadataResponse model."""

    compatibility_properties: Optional[List[CompatibilityProperty]] = Field(
        default=None, alias="compatibilityProperties"
    )
