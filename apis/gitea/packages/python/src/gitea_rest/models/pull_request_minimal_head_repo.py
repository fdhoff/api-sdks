# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class PullRequestMinimalHeadRepo(ApiModel):
    """PullRequestMinimalHeadRepo model."""

    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
