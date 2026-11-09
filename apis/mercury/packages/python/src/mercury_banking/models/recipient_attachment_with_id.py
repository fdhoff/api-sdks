# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.tax_form_type import TaxFormType
from mercury_banking._runtime import ApiModel


class RecipientAttachmentWithId(ApiModel):
    """RecipientAttachmentWithId model."""

    file_name: StrictStr = Field(alias="fileName")
    form_type: Optional[TaxFormType] = Field(default=None, alias="formType")
    id: UUID
    recipient_id: UUID = Field(alias="recipientId")
    uploaded_at: StrictStr = Field(alias="uploadedAt")
    url: StrictStr
