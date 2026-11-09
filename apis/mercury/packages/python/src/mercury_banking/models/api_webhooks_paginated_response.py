# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_webhook_response import ApiWebhookResponse
from mercury_banking.models.api_webhooks_paginated_response_page import ApiWebhooksPaginatedResponsePage
from mercury_banking._runtime import ApiModel


class ApiWebhooksPaginatedResponse(ApiModel):
    """ApiWebhooksPaginatedResponse model."""

    page: ApiWebhooksPaginatedResponsePage
    webhooks: List[ApiWebhookResponse]
