# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.action_workflow_run import ActionWorkflowRun
from gitea_rest._runtime import ApiModel


class ActionArtifact(ApiModel):
    """ActionArtifact model."""

    archive_download_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    expired: Optional[StrictBool] = None
    expires_at: Optional[datetime] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    size_in_bytes: Optional[StrictInt] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    workflow_run: Optional[ActionWorkflowRun] = None
