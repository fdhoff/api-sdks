# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking.models.api_user_role import ApiUserRole
from mercury_banking._runtime import ApiModel


class UserDetails(ApiModel):
    """UserDetails model."""

    email: StrictStr
    first_name: StrictStr = Field(alias="firstName")
    last_name: StrictStr = Field(alias="lastName")
    organization_role: ApiUserRole = Field(alias="organizationRole")
    user_id: UUID = Field(alias="userId")
