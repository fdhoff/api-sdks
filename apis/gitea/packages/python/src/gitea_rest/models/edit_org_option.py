# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.visibility_string import VisibilityString
from gitea_rest._runtime import ApiModel


class EditOrgOption(ApiModel):
    """EditOrgOption model."""

    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    repo_admin_change_team_access: Optional[StrictBool] = None
    visibility: Optional[VisibilityString] = None
    website: Optional[StrictStr] = None
