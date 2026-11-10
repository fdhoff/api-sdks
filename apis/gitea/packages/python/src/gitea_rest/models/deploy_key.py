# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.repository import Repository
from gitea_rest._runtime import ApiModel


class DeployKey(ApiModel):
    """DeployKey model."""

    created_at: Optional[datetime] = None
    fingerprint: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    key_id: Optional[StrictInt] = None
    key_type: Optional[StrictStr] = None
    read_only: Optional[StrictBool] = None
    repository: Optional[Repository] = None
    title: Optional[StrictStr] = None
    token: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
