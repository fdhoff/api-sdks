# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class PublicKey(ApiModel):
    """PublicKey model."""

    created_at: Optional[datetime] = None
    fingerprint: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    key_type: Optional[StrictStr] = None
    last_used_at: Optional[datetime] = None
    read_only: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
