# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.state_type import StateType
from gitea_rest._runtime import ApiModel


class CreateMilestoneOption(ApiModel):
    """CreateMilestoneOption model."""

    description: Optional[StrictStr] = None
    due_on: Optional[datetime] = None
    state: Optional[StateType] = None
    title: Optional[StrictStr] = None
