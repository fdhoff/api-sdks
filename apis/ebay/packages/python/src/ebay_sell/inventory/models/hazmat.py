# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Hazmat(ApiModel):
    """Hazmat model."""

    component: Optional[StrictStr] = None
    pictograms: Optional[List[StrictStr]] = None
    signal_word: Optional[StrictStr] = Field(default=None, alias="signalWord")
    statements: Optional[List[StrictStr]] = None
