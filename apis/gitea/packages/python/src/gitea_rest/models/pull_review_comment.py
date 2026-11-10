# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class PullReviewComment(ApiModel):
    """PullReviewComment model."""

    body: Optional[StrictStr] = None
    commit_id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    diff_hunk: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    original_commit_id: Optional[StrictStr] = None
    original_position: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    position: Optional[StrictInt] = None
    pull_request_review_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    resolver: Optional[User] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
