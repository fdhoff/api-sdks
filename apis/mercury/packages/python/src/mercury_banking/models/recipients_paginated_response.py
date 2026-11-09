# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.recipient_info import RecipientInfo
from mercury_banking.models.recipients_paginated_response_page import RecipientsPaginatedResponsePage
from mercury_banking._runtime import ApiModel


class RecipientsPaginatedResponse(ApiModel):
    """RecipientsPaginatedResponse model."""

    page: RecipientsPaginatedResponsePage
    recipients: List[RecipientInfo]
    total: Annotated[int, Field(le=1000, strict=True, ge=0)]
