# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class StopWatch(ApiModel):
    """StopWatch model."""

    created: Optional[datetime] = None
    duration: Optional[StrictStr] = None
    issue_index: Optional[StrictInt] = None
    issue_title: Optional[StrictStr] = None
    repo_name: Optional[StrictStr] = None
    repo_owner_name: Optional[StrictStr] = None
    seconds: Optional[StrictInt] = None
