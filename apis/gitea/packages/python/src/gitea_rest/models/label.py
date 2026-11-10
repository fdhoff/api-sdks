# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Label(ApiModel):
    """Label model."""

    color: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    exclusive: Optional[StrictBool] = None
    id: Optional[StrictInt] = None
    is_archived: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
