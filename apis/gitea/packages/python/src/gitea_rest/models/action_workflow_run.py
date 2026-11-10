# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.pull_request_minimal import PullRequestMinimal
from gitea_rest.models.repository import Repository
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class ActionWorkflowRun(ApiModel):
    """ActionWorkflowRun model."""

    actor: Optional[User] = None
    artifacts_url: Optional[StrictStr] = None
    cancel_url: Optional[StrictStr] = None
    completed_at: Optional[datetime] = None
    conclusion: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    display_title: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    head_branch: Optional[StrictStr] = None
    head_repository: Optional[Repository] = None
    head_sha: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    jobs_url: Optional[StrictStr] = None
    logs_url: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    previous_attempt_url: Optional[StrictStr] = None
    pull_requests: Optional[List[PullRequestMinimal]] = None
    repository: Optional[Repository] = None
    repository_id: Optional[StrictInt] = None
    rerun_url: Optional[StrictStr] = None
    run_attempt: Optional[StrictInt] = None
    run_number: Optional[StrictInt] = None
    started_at: Optional[datetime] = None
    status: Optional[StrictStr] = None
    trigger_actor: Optional[User] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
