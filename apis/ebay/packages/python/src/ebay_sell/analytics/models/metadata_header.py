# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.definition import Definition
from ebay_sell._runtime import ApiModel


class MetadataHeader(ApiModel):
    """MetadataHeader model."""

    key: Optional[StrictStr] = None
    metadata_keys: Optional[List[Definition]] = Field(default=None, alias="metadataKeys")
