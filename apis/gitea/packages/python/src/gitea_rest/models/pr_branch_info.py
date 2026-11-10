# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.repository import Repository
from gitea_rest._runtime import ApiModel


class PRBranchInfo(ApiModel):
    """PRBranchInfo model."""

    label: Optional[StrictStr] = None
    ref: Optional[StrictStr] = None
    repo: Optional[Repository] = None
    repo_id: Optional[StrictInt] = None
    sha: Optional[StrictStr] = None
