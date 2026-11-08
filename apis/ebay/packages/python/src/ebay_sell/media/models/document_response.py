# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.media.models.document_metadata import DocumentMetadata
from ebay_sell._runtime import ApiModel


class DocumentResponse(ApiModel):
    """DocumentResponse model."""

    document_id: Optional[StrictStr] = Field(default=None, alias="documentId")
    document_metadata: Optional[DocumentMetadata] = Field(default=None, alias="documentMetadata")
    document_status: Optional[StrictStr] = Field(default=None, alias="documentStatus")
    document_type: Optional[StrictStr] = Field(default=None, alias="documentType")
    languages: Optional[List[StrictStr]] = None
