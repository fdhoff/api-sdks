# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.metadata_header import MetadataHeader
from ebay_sell.analytics.models.metadata_record import MetadataRecord
from ebay_sell._runtime import ApiModel


class Metadata(ApiModel):
    """Metadata model."""

    metadata_header: Optional[MetadataHeader] = Field(default=None, alias="metadataHeader")
    metadata_records: Optional[List[MetadataRecord]] = Field(default=None, alias="metadataRecords")
