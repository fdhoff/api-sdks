# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.team import Team
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class RepoTransfer(ApiModel):
    """RepoTransfer model."""

    doer: Optional[User] = None
    recipient: Optional[User] = None
    teams: Optional[List[Team]] = None
