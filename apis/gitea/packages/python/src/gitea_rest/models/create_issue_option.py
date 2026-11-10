# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreateIssueOption(ApiModel):
    """CreateIssueOption model."""

    assignee: Optional[StrictStr] = None
    assignees: Optional[List[StrictStr]] = None
    body: Optional[StrictStr] = None
    closed: Optional[StrictBool] = None
    due_date: Optional[datetime] = None
    labels: Optional[List[StrictInt]] = None
    milestone: Optional[StrictInt] = None
    projects: Optional[List[StrictInt]] = None
    ref: Optional[StrictStr] = None
    title: StrictStr
