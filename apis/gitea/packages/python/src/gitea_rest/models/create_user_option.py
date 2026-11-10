# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.visibility_string import VisibilityString
from gitea_rest._runtime import ApiModel


class CreateUserOption(ApiModel):
    """CreateUserOption model."""

    created_at: Optional[datetime] = None
    email: StrictStr
    full_name: Optional[StrictStr] = None
    login_name: Optional[StrictStr] = None
    must_change_password: Optional[StrictBool] = None
    password: Optional[StrictStr] = None
    restricted: Optional[StrictBool] = None
    send_notify: Optional[StrictBool] = None
    source_id: Optional[StrictInt] = None
    username: StrictStr
    visibility: Optional[VisibilityString] = None
