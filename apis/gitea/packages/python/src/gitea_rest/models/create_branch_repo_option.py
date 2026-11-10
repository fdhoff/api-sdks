# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gitea_rest._runtime import ApiModel


class CreateBranchRepoOption(ApiModel):
    """CreateBranchRepoOption model."""

    new_branch_name: Annotated[str, Field(strict=True)]
    old_branch_name: Optional[Annotated[str, Field(strict=True)]] = None
    old_ref_name: Optional[Annotated[str, Field(strict=True)]] = None
