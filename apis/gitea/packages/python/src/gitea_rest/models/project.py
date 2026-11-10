# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.state_type import StateType
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Project(ApiModel):
    """Project model."""

    card_type: Optional[StrictStr] = None
    closed_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    creator_id: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_closed: Optional[StrictBool] = None
    num_closed_issues: Optional[StrictInt] = None
    num_issues: Optional[StrictInt] = None
    num_open_issues: Optional[StrictInt] = None
    owner_id: Optional[StrictInt] = None
    repo_id: Optional[StrictInt] = None
    state: Optional[StateType] = None
    template_type: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
