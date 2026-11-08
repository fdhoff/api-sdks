# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class EvaluationCycle(ApiModel):
    """EvaluationCycle model."""

    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    evaluation_date: Optional[StrictStr] = Field(default=None, alias="evaluationDate")
    evaluation_type: Optional[StrictStr] = Field(default=None, alias="evaluationType")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
