# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Cycle(ApiModel):
    """Cycle model."""

    cycle_type: Optional[StrictStr] = Field(default=None, alias="cycleType")
    evaluation_date: Optional[StrictStr] = Field(default=None, alias="evaluationDate")
    evaluation_month: Optional[StrictStr] = Field(default=None, alias="evaluationMonth")
