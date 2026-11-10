# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.access_level_name import AccessLevelName
from gitea_rest.models.organization import Organization
from gitea_rest.models.team_visibility import TeamVisibility
from gitea_rest._runtime import ApiModel


class Team(ApiModel):
    """Team model."""

    can_create_org_repo: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    includes_all_repositories: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    organization: Optional[Organization] = None
    permission: Optional[AccessLevelName] = None
    units: Optional[List[StrictStr]] = None
    units_map: Optional[Dict[str, StrictStr]] = None
    visibility: Optional[TeamVisibility] = None
