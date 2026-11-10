# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_status import CommitStatus
from gitea_rest.models.commit_status_state import CommitStatusState
from gitea_rest.models.repository import Repository
from gitea_rest._runtime import ApiModel


class CombinedStatus(ApiModel):
    """CombinedStatus model."""

    commit_url: Optional[StrictStr] = None
    repository: Optional[Repository] = None
    sha: Optional[StrictStr] = None
    state: Optional[CommitStatusState] = None
    statuses: Optional[List[CommitStatus]] = None
    total_count: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
