# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_event_response import ApiEventResponse
from mercury_banking.models.api_events_paginated_response_page import ApiEventsPaginatedResponsePage
from mercury_banking._runtime import ApiModel


class ApiEventsPaginatedResponse(ApiModel):
    """ApiEventsPaginatedResponse model."""

    events: List[ApiEventResponse]
    page: ApiEventsPaginatedResponsePage
