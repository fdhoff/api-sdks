# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_meta import CommitMeta
from gitea_rest.models.commit_user import CommitUser
from gitea_rest._runtime import ApiModel


class FileCommitResponse(ApiModel):
    """FileCommitResponse model."""

    author: Optional[CommitUser] = None
    committer: Optional[CommitUser] = None
    created: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    parents: Optional[List[CommitMeta]] = None
    sha: Optional[StrictStr] = None
    tree: Optional[CommitMeta] = None
    url: Optional[StrictStr] = None
