# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_ar_attachment_response_data import ApiV1ArAttachmentResponseData
from mercury_banking._runtime import ApiModel


class ApiV1ArAttachmentsResponseData(ApiModel):
    """ApiV1ArAttachmentsResponseData model."""

    attachments: List[ApiV1ArAttachmentResponseData]
