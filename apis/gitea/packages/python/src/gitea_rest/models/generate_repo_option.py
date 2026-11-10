# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gitea_rest._runtime import ApiModel


class GenerateRepoOption(ApiModel):
    """GenerateRepoOption model."""

    avatar: Optional[StrictBool] = None
    default_branch: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    git_content: Optional[StrictBool] = None
    git_hooks: Optional[StrictBool] = None
    labels: Optional[StrictBool] = None
    name: Annotated[str, Field(strict=True)]
    owner: StrictStr
    private: Optional[StrictBool] = None
    protected_branch: Optional[StrictBool] = None
    topics: Optional[StrictBool] = None
    webhooks: Optional[StrictBool] = None
