# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_status_state import CommitStatusState
from gitea_rest._runtime import ApiModel


class CreateStatusOption(ApiModel):
    """CreateStatusOption model."""

    context: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    state: Optional[CommitStatusState] = None
    target_url: Optional[StrictStr] = None
