# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class LightAttachment(ApiModel):
    """LightAttachment model."""

    id: Optional[StrictInt] = None
    attachment: Optional[StrictStr] = None
    date_creation: Optional[datetime] = None
