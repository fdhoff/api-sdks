# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class FileInfo(ApiModel):
    """FileInfo model."""

    file_id: Optional[StrictStr] = Field(default=None, alias="fileId")
    file_type: Optional[StrictStr] = Field(default=None, alias="fileType")
    name: Optional[StrictStr] = None
    uploaded_date: Optional[StrictStr] = Field(default=None, alias="uploadedDate")
