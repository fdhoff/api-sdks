# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.access_level_name import AccessLevelName
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class RepoCollaboratorPermission(ApiModel):
    """RepoCollaboratorPermission model."""

    permission: Optional[AccessLevelName] = None
    role_name: Optional[StrictStr] = None
    user: Optional[User] = None
