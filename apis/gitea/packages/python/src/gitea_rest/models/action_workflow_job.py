# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.action_workflow_step import ActionWorkflowStep
from gitea_rest._runtime import ApiModel


class ActionWorkflowJob(ApiModel):
    """ActionWorkflowJob model."""

    completed_at: Optional[datetime] = None
    conclusion: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    head_branch: Optional[StrictStr] = None
    head_sha: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    labels: Optional[List[StrictStr]] = None
    name: Optional[StrictStr] = None
    run_attempt: Optional[StrictInt] = None
    run_id: Optional[StrictInt] = None
    run_url: Optional[StrictStr] = None
    runner_id: Optional[StrictInt] = None
    runner_name: Optional[StrictStr] = None
    started_at: Optional[datetime] = None
    status: Optional[StrictStr] = None
    steps: Optional[List[ActionWorkflowStep]] = None
    url: Optional[StrictStr] = None
