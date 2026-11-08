# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.value import Value
from ebay_sell._runtime import ApiModel


class MetadataRecord(ApiModel):
    """MetadataRecord model."""

    metadata_values: Optional[List[Value]] = Field(default=None, alias="metadataValues")
    value: Optional[Value] = None
