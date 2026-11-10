# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class WatchInfo(ApiModel):
    """WatchInfo model."""

    created_at: Optional[datetime] = None
    ignored: Optional[StrictBool] = None
    reason: Optional[Any] = None
    repository_url: Optional[StrictStr] = None
    subscribed: Optional[StrictBool] = None
    url: Optional[StrictStr] = None
