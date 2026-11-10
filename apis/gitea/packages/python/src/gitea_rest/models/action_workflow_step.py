# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ActionWorkflowStep(ApiModel):
    """ActionWorkflowStep model."""

    completed_at: Optional[datetime] = None
    conclusion: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    number: Optional[StrictInt] = None
    started_at: Optional[datetime] = None
    status: Optional[StrictStr] = None
