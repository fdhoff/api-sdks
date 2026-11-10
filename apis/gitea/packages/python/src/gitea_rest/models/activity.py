# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.comment import Comment
from gitea_rest.models.repository import Repository
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Activity(ApiModel):
    """Activity model."""

    act_user: Optional[User] = None
    act_user_id: Optional[StrictInt] = None
    comment: Optional[Comment] = None
    comment_id: Optional[StrictInt] = None
    content: Optional[StrictStr] = None
    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    is_private: Optional[StrictBool] = None
    op_type: Optional[StrictStr] = None
    ref_name: Optional[StrictStr] = None
    repo: Optional[Repository] = None
    repo_id: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = None
