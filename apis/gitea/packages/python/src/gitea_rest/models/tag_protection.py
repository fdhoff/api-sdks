# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class TagProtection(ApiModel):
    """TagProtection model."""

    created_at: Optional[datetime] = None
    id: Optional[StrictInt] = None
    name_pattern: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    whitelist_teams: Optional[List[StrictStr]] = None
    whitelist_usernames: Optional[List[StrictStr]] = None
