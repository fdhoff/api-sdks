# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.attachment import Attachment
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Comment(ApiModel):
    """Comment model."""

    assets: Optional[List[Attachment]] = None
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    issue_url: Optional[StrictStr] = None
    original_author: Optional[StrictStr] = None
    original_author_id: Optional[StrictInt] = None
    pull_request_url: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    user: Optional[User] = None
