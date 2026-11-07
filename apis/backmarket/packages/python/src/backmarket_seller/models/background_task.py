# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class BackgroundTask(ApiModel):
    """BackgroundTask model."""

    task_id: StrictInt
    action_status: StrictInt
    last_action_error: Optional[StrictStr]
    result: Optional[Any]
    statuscode: StrictInt
