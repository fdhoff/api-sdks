# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.create_pull_review_comment import CreatePullReviewComment
from gitea_rest.models.review_state_type import ReviewStateType
from gitea_rest._runtime import ApiModel


class CreatePullReviewOptions(ApiModel):
    """CreatePullReviewOptions model."""

    body: Optional[StrictStr] = None
    comments: Optional[List[CreatePullReviewComment]] = None
    commit_id: Optional[StrictStr] = None
    event: Optional[ReviewStateType] = None
