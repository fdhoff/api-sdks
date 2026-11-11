# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.api_user_role import ApiUserRole
from mercury_banking._runtime import ApiModel


class UserDetails(ApiModel):
    """UserDetails model."""

    email: StrictStr
    first_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="firstName")
    last_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="lastName")
    organization_role: ApiUserRole = Field(alias="organizationRole")
    user_id: UUID = Field(alias="userId")
