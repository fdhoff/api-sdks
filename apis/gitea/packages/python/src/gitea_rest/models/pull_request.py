# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.label import Label
from gitea_rest.models.milestone import Milestone
from gitea_rest.models.pr_branch_info import PRBranchInfo
from gitea_rest.models.state_type import StateType
from gitea_rest.models.team import Team
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class PullRequest(ApiModel):
    """PullRequest model."""

    additions: Optional[StrictInt] = None
    allow_maintainer_edit: Optional[StrictBool] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = None
    base: Optional[PRBranchInfo] = None
    body: Optional[StrictStr] = None
    changed_files: Optional[StrictInt] = None
    closed_at: Optional[datetime] = None
    comments: Optional[StrictInt] = None
    content_version: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    deletions: Optional[StrictInt] = None
    diff_url: Optional[StrictStr] = None
    draft: Optional[StrictBool] = None
    due_date: Optional[datetime] = None
    head: Optional[PRBranchInfo] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_locked: Optional[StrictBool] = None
    labels: Optional[List[Label]] = None
    merge_base: Optional[StrictStr] = None
    merge_commit_sha: Optional[StrictStr] = None
    mergeable: Optional[StrictBool] = None
    merged: Optional[StrictBool] = None
    merged_at: Optional[datetime] = None
    merged_by: Optional[User] = None
    milestone: Optional[Milestone] = None
    number: Optional[StrictInt] = None
    patch_url: Optional[StrictStr] = None
    pin_order: Optional[StrictInt] = None
    requested_reviewers: Optional[List[User]] = None
    requested_reviewers_teams: Optional[List[Team]] = None
    review_comments: Optional[StrictInt] = None
    state: Optional[StateType] = None
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
