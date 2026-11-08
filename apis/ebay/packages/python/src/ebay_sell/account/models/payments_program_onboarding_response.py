# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.payments_program_onboarding_steps import PaymentsProgramOnboardingSteps
from ebay_sell._runtime import ApiModel


class PaymentsProgramOnboardingResponse(ApiModel):
    """PaymentsProgramOnboardingResponse model."""

    onboarding_status: Optional[StrictStr] = Field(default=None, alias="onboardingStatus")
    steps: Optional[List[PaymentsProgramOnboardingSteps]] = None
