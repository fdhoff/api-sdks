# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class APIOnboardingDataAbout(ApiModel):
    """APIOnboardingDataAbout model."""

    countries_of_operations: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(
        default=None, alias="countriesOfOperations"
    )
    country_of_operation: Optional[StrictStr] = Field(default=None, alias="countryOfOperation")
    description: Optional[StrictStr] = None
    industry: Optional[StrictStr] = None
    legal_business_name: Optional[StrictStr] = Field(default=None, alias="legalBusinessName")
    website: Optional[StrictStr] = None
