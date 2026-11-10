# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Secret(ApiModel):
    """Secret model."""

    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
