# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ActionWorkflow(ApiModel):
    """ActionWorkflow model."""

    badge_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
