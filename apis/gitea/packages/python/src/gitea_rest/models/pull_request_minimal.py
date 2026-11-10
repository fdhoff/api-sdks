# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.pull_request_minimal_head import PullRequestMinimalHead
from gitea_rest._runtime import ApiModel


class PullRequestMinimal(ApiModel):
    """PullRequestMinimal model."""

    base: Optional[PullRequestMinimalHead] = None
    head: Optional[PullRequestMinimalHead] = None
    id: Optional[StrictInt] = None
    number: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
