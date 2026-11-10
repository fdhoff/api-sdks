# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreatePushMirrorOption(ApiModel):
    """CreatePushMirrorOption model."""

    interval: Optional[StrictStr] = None
    remote_address: Optional[StrictStr] = None
    remote_password: Optional[StrictStr] = None
    remote_username: Optional[StrictStr] = None
    sync_on_commit: Optional[StrictBool] = None
