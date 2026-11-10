# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.git_entry import GitEntry
from gitea_rest._runtime import ApiModel


class GitTreeResponse(ApiModel):
    """GitTreeResponse model."""

    page: Optional[StrictInt] = None
    sha: Optional[StrictStr] = None
    total_count: Optional[StrictInt] = None
    tree: Optional[List[GitEntry]] = None
    truncated: Optional[StrictBool] = None
    url: Optional[StrictStr] = None
