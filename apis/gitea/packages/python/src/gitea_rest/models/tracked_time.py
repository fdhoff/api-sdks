# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.issue import Issue
from gitea_rest._runtime import ApiModel


class TrackedTime(ApiModel):
    """TrackedTime model."""

    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    issue: Optional[Issue] = None
    issue_id: Optional[StrictInt] = None
    time: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = None
    user_name: Optional[StrictStr] = None
