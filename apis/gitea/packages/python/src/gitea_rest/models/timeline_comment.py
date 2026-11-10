# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.comment import Comment
from gitea_rest.models.issue import Issue
from gitea_rest.models.label import Label
from gitea_rest.models.milestone import Milestone
from gitea_rest.models.team import Team
from gitea_rest.models.tracked_time import TrackedTime
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class TimelineComment(ApiModel):
    """TimelineComment model."""

    assignee: Optional[User] = None
    assignee_team: Optional[Team] = None
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    dependent_issue: Optional[Issue] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    issue_url: Optional[StrictStr] = None
    label: Optional[Label] = None
    milestone: Optional[Milestone] = None
    new_ref: Optional[StrictStr] = None
    new_title: Optional[StrictStr] = None
    old_milestone: Optional[Milestone] = None
    old_project_id: Optional[StrictInt] = None
    old_ref: Optional[StrictStr] = None
    old_title: Optional[StrictStr] = None
    project_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    ref_action: Optional[StrictStr] = None
    ref_comment: Optional[Comment] = None
    ref_commit_sha: Optional[StrictStr] = None
    ref_issue: Optional[Issue] = None
    removed_assignee: Optional[StrictBool] = None
    resolve_doer: Optional[User] = None
    review_id: Optional[StrictInt] = None
    tracked_time: Optional[TrackedTime] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
