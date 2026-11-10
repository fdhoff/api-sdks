# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user_type_string import UserTypeString
from gitea_rest.models.visibility_string import VisibilityString
from gitea_rest._runtime import ApiModel


class EditUserOption(ApiModel):
    """EditUserOption model."""

    active: Optional[StrictBool] = None
    admin: Optional[StrictBool] = None
    allow_create_organization: Optional[StrictBool] = None
    allow_git_hook: Optional[StrictBool] = None
    allow_import_local: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    login_name: Optional[StrictStr] = None
    max_repo_creation: Optional[StrictInt] = None
    must_change_password: Optional[StrictBool] = None
    password: Optional[StrictStr] = None
    prohibit_login: Optional[StrictBool] = None
    restricted: Optional[StrictBool] = None
    source_id: StrictInt
    type: Optional[UserTypeString] = None
    visibility: Optional[VisibilityString] = None
    website: Optional[StrictStr] = None
