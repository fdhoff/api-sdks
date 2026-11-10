# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_affected_files import CommitAffectedFiles
from gitea_rest.models.commit_meta import CommitMeta
from gitea_rest.models.commit_stats import CommitStats
from gitea_rest.models.repo_commit import RepoCommit
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Commit(ApiModel):
    """Commit model."""

    author: Optional[User] = None
    commit: Optional[RepoCommit] = None
    committer: Optional[User] = None
    created: Optional[datetime] = None
    files: Optional[List[CommitAffectedFiles]] = None
    html_url: Optional[StrictStr] = None
    parents: Optional[List[CommitMeta]] = None
    sha: Optional[StrictStr] = None
    stats: Optional[CommitStats] = None
    url: Optional[StrictStr] = None
