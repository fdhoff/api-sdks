# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class ProjectColumn(ApiModel):
    """ProjectColumn model."""

    color: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    default: Optional[StrictBool] = None
    id: Optional[StrictInt] = None
    project_id: Optional[StrictInt] = None
    sorting: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
