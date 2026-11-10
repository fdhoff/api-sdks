# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class UpdateBranchRepoOption(ApiModel):
    """UpdateBranchRepoOption model."""

    force: Optional[StrictBool] = None
    new_commit_id: StrictStr
    old_commit_id: Optional[StrictStr] = None
