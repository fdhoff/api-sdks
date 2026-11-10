# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Reaction(ApiModel):
    """Reaction model."""

    content: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    user: Optional[User] = None
