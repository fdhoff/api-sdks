# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.cycle import Cycle
from ebay_sell.analytics.models.metric import Metric
from ebay_sell._runtime import ApiModel


class StandardsProfile(ApiModel):
    """StandardsProfile model."""

    cycle: Optional[Cycle] = None
    default_program: Optional[StrictBool] = Field(default=None, alias="defaultProgram")
    evaluation_reason: Optional[StrictStr] = Field(default=None, alias="evaluationReason")
    metrics: Optional[List[Metric]] = None
    program: Optional[StrictStr] = None
    standards_level: Optional[StrictStr] = Field(default=None, alias="standardsLevel")
