# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.attachment import Attachment
from gitea_rest.models.label import Label
from gitea_rest.models.milestone import Milestone
from gitea_rest.models.project import Project
from gitea_rest.models.pull_request_meta import PullRequestMeta
from gitea_rest.models.repository_meta import RepositoryMeta
from gitea_rest.models.state_type import StateType
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Issue(ApiModel):
    """Issue model."""

    assets: Optional[List[Attachment]] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = None
    body: Optional[StrictStr] = None
    closed_at: Optional[datetime] = None
    comments: Optional[StrictInt] = None
    content_version: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_locked: Optional[StrictBool] = None
    labels: Optional[List[Label]] = None
    milestone: Optional[Milestone] = None
    number: Optional[StrictInt] = None
    original_author: Optional[StrictStr] = None
    original_author_id: Optional[StrictInt] = None
    pin_order: Optional[StrictInt] = None
    projects: Optional[List[Project]] = None
    pull_request: Optional[PullRequestMeta] = None
    ref: Optional[StrictStr] = None
    repository: Optional[RepositoryMeta] = None
    state: Optional[StateType] = None
    time_estimate: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
