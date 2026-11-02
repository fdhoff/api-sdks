# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class ReturnLabel(ApiModel):
    """ReturnLabel model."""

    date_creation: Optional[datetime] = None
    state: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    initiator: Optional[StrictStr] = None
    kind: Optional[StrictStr] = None
