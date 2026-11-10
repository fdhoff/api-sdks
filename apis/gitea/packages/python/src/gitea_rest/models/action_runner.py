# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.action_runner_label import ActionRunnerLabel
from gitea_rest._runtime import ApiModel


class ActionRunner(ApiModel):
    """ActionRunner model."""

    busy: Optional[StrictBool] = None
    disabled: Optional[StrictBool] = None
    ephemeral: Optional[StrictBool] = None
    id: Optional[StrictInt] = None
    labels: Optional[List[ActionRunnerLabel]] = None
    name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
