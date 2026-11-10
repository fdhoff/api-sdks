# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.repo_write_permission import RepoWritePermission
from gitea_rest.models.team_visibility import TeamVisibility
from gitea_rest._runtime import ApiModel


class EditTeamOption(ApiModel):
    """EditTeamOption model."""

    can_create_org_repo: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    includes_all_repositories: Optional[StrictBool] = None
    name: StrictStr
    permission: Optional[RepoWritePermission] = None
    units: Optional[List[StrictStr]] = None
    units_map: Optional[Dict[str, StrictStr]] = None
    visibility: Optional[TeamVisibility] = None
