# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.recipient_invite_api_paginated_response_page import RecipientInviteApiPaginatedResponsePage
from mercury_banking.models.recipient_invite_api_response import RecipientInviteApiResponse
from mercury_banking._runtime import ApiModel


class RecipientInviteApiPaginatedResponse(ApiModel):
    """RecipientInviteApiPaginatedResponse model."""

    invites: List[RecipientInviteApiResponse]
    page: RecipientInviteApiPaginatedResponsePage
