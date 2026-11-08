# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PaymentsProgramOnboardingSteps(ApiModel):
    """PaymentsProgramOnboardingSteps model."""

    name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    web_url: Optional[StrictStr] = Field(default=None, alias="webUrl")
