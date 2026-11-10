# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.repository import Repository
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Package(ApiModel):
    """Package model."""

    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    owner: Optional[User] = None
    repository: Optional[Repository] = None
    type: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
