# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ActionTask(ApiModel):
    """ActionTask model."""

    created_at: Optional[datetime] = None
    display_title: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    head_branch: Optional[StrictStr] = None
    head_sha: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    run_number: Optional[StrictInt] = None
    run_started_at: Optional[datetime] = None
    status: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    workflow_id: Optional[StrictStr] = None
