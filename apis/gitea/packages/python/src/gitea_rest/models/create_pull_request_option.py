# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreatePullRequestOption(ApiModel):
    """CreatePullRequestOption model."""

    allow_maintainer_edit: Optional[StrictBool] = None
    assignee: Optional[StrictStr] = None
    assignees: Optional[List[StrictStr]] = None
    base: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    due_date: Optional[datetime] = None
    head: Optional[StrictStr] = None
    labels: Optional[List[StrictInt]] = None
    milestone: Optional[StrictInt] = None
    reviewers: Optional[List[StrictStr]] = None
    team_reviewers: Optional[List[StrictStr]] = None
    title: Optional[StrictStr] = None
