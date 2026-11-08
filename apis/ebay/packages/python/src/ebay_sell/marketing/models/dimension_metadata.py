# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.dimension_key_annotation import DimensionKeyAnnotation
from ebay_sell._runtime import ApiModel


class DimensionMetadata(ApiModel):
    """DimensionMetadata model."""

    data_type: Optional[StrictStr] = Field(default=None, alias="dataType")
    dimension_key: Optional[StrictStr] = Field(default=None, alias="dimensionKey")
    dimension_key_annotations: Optional[List[DimensionKeyAnnotation]] = Field(
        default=None, alias="dimensionKeyAnnotations"
    )
