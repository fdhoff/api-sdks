# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreateHookOption(ApiModel):
    """CreateHookOption model."""

    active: Optional[StrictBool] = False
    authorization_header: Optional[StrictStr] = None
    branch_filter: Optional[StrictStr] = None
    config: Dict[str, StrictStr]
    events: Optional[List[StrictStr]] = None
    name: Optional[StrictStr] = None
    type: StrictStr
