# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class UploadedAttachment(ApiModel):
    """UploadedAttachment model."""

    attachment_id: Optional[StrictStr] = Field(default=None, alias="attachmentId")
    download_url: Optional[StrictStr] = Field(default=None, alias="downloadUrl")
