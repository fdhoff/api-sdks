# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking._runtime import ApiModel


class APISubmitOnboardingDataResponse(ApiModel):
    """APISubmitOnboardingDataResponse model."""

    onboarding_data_id: UUID = Field(alias="onboardingDataId")
    signup_link: StrictStr = Field(alias="signupLink")
