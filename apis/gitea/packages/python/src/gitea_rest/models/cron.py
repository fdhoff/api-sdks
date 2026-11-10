# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Cron(ApiModel):
    """Cron model."""

    exec_times: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    next: Optional[datetime] = None
    prev: Optional[datetime] = None
    schedule: Optional[StrictStr] = None
