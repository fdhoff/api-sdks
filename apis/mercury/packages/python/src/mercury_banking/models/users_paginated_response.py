# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.user_details import UserDetails
from mercury_banking.models.users_paginated_response_page import UsersPaginatedResponsePage
from mercury_banking._runtime import ApiModel


class UsersPaginatedResponse(ApiModel):
    """UsersPaginatedResponse model."""

    page: UsersPaginatedResponsePage
    users: List[UserDetails]
