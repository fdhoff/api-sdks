# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user_type_string import UserTypeString
from gitea_rest.models.visibility_string import VisibilityString
from gitea_rest._runtime import ApiModel


class User(ApiModel):
    """User model."""

    active: Optional[StrictBool] = None
    avatar_url: Optional[StrictStr] = None
    created: Optional[datetime] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    followers_count: Optional[StrictInt] = None
    following_count: Optional[StrictInt] = None
    full_name: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_admin: Optional[StrictBool] = None
    language: Optional[StrictStr] = None
    last_login: Optional[datetime] = None
    location: Optional[StrictStr] = None
    login: Optional[StrictStr] = None
    login_name: Optional[StrictStr] = None
    prohibit_login: Optional[StrictBool] = None
    restricted: Optional[StrictBool] = None
    source_id: Optional[StrictInt] = None
    starred_repos_count: Optional[StrictInt] = None
    type: Optional[UserTypeString] = None
    visibility: Optional[VisibilityString] = None
    website: Optional[StrictStr] = None
