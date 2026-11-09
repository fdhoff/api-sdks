# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.recipient_attachment_with_id import RecipientAttachmentWithId
from mercury_banking.models.recipients_attachments_paginated_response_page import (
    RecipientsAttachmentsPaginatedResponsePage,
)
from mercury_banking._runtime import ApiModel


class RecipientsAttachmentsPaginatedResponse(ApiModel):
    """RecipientsAttachmentsPaginatedResponse model."""

    attachments: List[RecipientAttachmentWithId]
    page: RecipientsAttachmentsPaginatedResponsePage
    total: Annotated[int, Field(le=1000, strict=True, ge=0)]
