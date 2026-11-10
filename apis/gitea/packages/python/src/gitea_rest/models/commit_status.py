# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_status_state import CommitStatusState
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class CommitStatus(ApiModel):
    """CommitStatus model."""

    context: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    status: Optional[CommitStatusState] = None
    target_url: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
