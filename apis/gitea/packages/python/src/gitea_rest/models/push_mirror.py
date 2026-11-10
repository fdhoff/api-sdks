# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class PushMirror(ApiModel):
    """PushMirror model."""

    created: Optional[datetime] = None
    interval: Optional[StrictStr] = None
    last_error: Optional[StrictStr] = None
    last_update: Optional[datetime] = None
    remote_address: Optional[StrictStr] = None
    remote_name: Optional[StrictStr] = None
    repo_name: Optional[StrictStr] = None
    sync_on_commit: Optional[StrictBool] = None
