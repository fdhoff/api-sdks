# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Hook(ApiModel):
    """Hook model."""

    active: Optional[StrictBool] = None
    authorization_header: Optional[StrictStr] = None
    branch_filter: Optional[StrictStr] = None
    config: Optional[Dict[str, StrictStr]] = None
    created_at: Optional[datetime] = None
    events: Optional[List[StrictStr]] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
