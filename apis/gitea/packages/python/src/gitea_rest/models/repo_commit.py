# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_meta import CommitMeta
from gitea_rest.models.commit_user import CommitUser
from gitea_rest.models.payload_commit_verification import PayloadCommitVerification
from gitea_rest._runtime import ApiModel


class RepoCommit(ApiModel):
    """RepoCommit model."""

    author: Optional[CommitUser] = None
    committer: Optional[CommitUser] = None
    message: Optional[StrictStr] = None
    tree: Optional[CommitMeta] = None
    url: Optional[StrictStr] = None
    verification: Optional[PayloadCommitVerification] = None
