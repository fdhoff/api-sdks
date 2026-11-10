# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.action_runner import ActionRunner
from gitea_rest._runtime import ApiModel


class ActionRunnersResponse(ApiModel):
    """ActionRunnersResponse model."""

    runners: Optional[List[ActionRunner]] = None
    total_count: Optional[StrictInt] = None
