# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.action_workflow import ActionWorkflow
from gitea_rest._runtime import ApiModel


class ActionWorkflowResponse(ApiModel):
    """ActionWorkflowResponse model."""

    total_count: Optional[StrictInt] = None
    workflows: Optional[List[ActionWorkflow]] = None
