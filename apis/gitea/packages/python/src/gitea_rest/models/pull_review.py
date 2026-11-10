# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.review_state_type import ReviewStateType
from gitea_rest.models.team import Team
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class PullReview(ApiModel):
    """PullReview model."""

    body: Optional[StrictStr] = None
    comments_count: Optional[StrictInt] = None
    commit_id: Optional[StrictStr] = None
    dismissed: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    official: Optional[StrictBool] = None
    pull_request_url: Optional[StrictStr] = None
    stale: Optional[StrictBool] = None
    state: Optional[ReviewStateType] = None
    submitted_at: Optional[datetime] = None
    team: Optional[Team] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
