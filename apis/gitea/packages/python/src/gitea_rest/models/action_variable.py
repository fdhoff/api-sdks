# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ActionVariable(ApiModel):
    """ActionVariable model."""

    data: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    owner_id: Optional[StrictInt] = None
    repo_id: Optional[StrictInt] = None
