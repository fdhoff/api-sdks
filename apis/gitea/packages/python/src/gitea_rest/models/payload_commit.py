# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.payload_commit_verification import PayloadCommitVerification
from gitea_rest.models.payload_user import PayloadUser
from gitea_rest._runtime import ApiModel


class PayloadCommit(ApiModel):
    """PayloadCommit model."""

    added: Optional[List[StrictStr]] = None
    author: Optional[PayloadUser] = None
    committer: Optional[PayloadUser] = None
    id: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    modified: Optional[List[StrictStr]] = None
    removed: Optional[List[StrictStr]] = None
    timestamp: Optional[datetime] = None
    url: Optional[StrictStr] = None
    verification: Optional[PayloadCommitVerification] = None
