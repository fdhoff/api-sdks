# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CommitStats(ApiModel):
    """CommitStats model."""

    additions: Optional[StrictInt] = None
    deletions: Optional[StrictInt] = None
    total: Optional[StrictInt] = None
