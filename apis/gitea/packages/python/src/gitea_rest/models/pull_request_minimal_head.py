# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.pull_request_minimal_head_repo import PullRequestMinimalHeadRepo
from gitea_rest._runtime import ApiModel


class PullRequestMinimalHead(ApiModel):
    """PullRequestMinimalHead model."""

    ref: Optional[StrictStr] = None
    repo: Optional[PullRequestMinimalHeadRepo] = None
    sha: Optional[StrictStr] = None
