# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreateLabelOption(ApiModel):
    """CreateLabelOption model."""

    color: StrictStr
    description: Optional[StrictStr] = None
    exclusive: Optional[StrictBool] = None
    is_archived: Optional[StrictBool] = None
    name: StrictStr
