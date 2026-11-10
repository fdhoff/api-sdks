# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_user import CommitUser
from gitea_rest._runtime import ApiModel


class WikiCommit(ApiModel):
    """WikiCommit model."""

    author: Optional[CommitUser] = None
    commiter: Optional[CommitUser] = None
    message: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
