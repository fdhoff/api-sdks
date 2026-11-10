# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class EditIssueOption(ApiModel):
    """EditIssueOption model."""

    assignee: Optional[StrictStr] = None
    assignees: Optional[List[StrictStr]] = None
    body: Optional[StrictStr] = None
    content_version: Optional[StrictInt] = None
    due_date: Optional[datetime] = None
    milestone: Optional[StrictInt] = None
    projects: Optional[List[StrictInt]] = None
    ref: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    unset_due_date: Optional[StrictBool] = None
