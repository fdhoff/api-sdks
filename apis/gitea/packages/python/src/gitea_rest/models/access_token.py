# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class AccessToken(ApiModel):
    """AccessToken model."""

    created_at: Optional[datetime] = None
    id: Optional[StrictInt] = None
    last_used_at: Optional[datetime] = None
    name: Optional[StrictStr] = None
    scopes: Optional[List[StrictStr]] = None
    sha1: Optional[StrictStr] = None
    token_last_eight: Optional[StrictStr] = None
