# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.transaction_attachment_type import TransactionAttachmentType
from mercury_banking._runtime import ApiModel


class TransactionAttachment(ApiModel):
    """TransactionAttachment model."""

    attachment_type: TransactionAttachmentType = Field(alias="attachmentType")
    file_name: StrictStr = Field(alias="fileName")
    url: StrictStr
