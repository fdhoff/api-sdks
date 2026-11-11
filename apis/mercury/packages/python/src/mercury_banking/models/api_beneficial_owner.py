# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.beneficial_owner_job_title import BeneficialOwnerJobTitle
from mercury_banking.models.citizenship_status import CitizenshipStatus
from mercury_banking.models.identification_type import IdentificationType
from mercury_banking.models.is_pep import IsPep
from mercury_banking._runtime import ApiModel


class APIBeneficialOwner(ApiModel):
    """APIBeneficialOwner model."""

    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    citizenship_status: Optional[CitizenshipStatus] = Field(default=None, alias="citizenshipStatus")
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    date_of_birth: Optional[date] = Field(default=None, alias="dateOfBirth")
    email: Optional[StrictStr] = None
    first_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = Field(
        default=None, alias="firstName"
    )
    identification_blob: Optional[StrictStr] = Field(default=None, alias="identificationBlob")
    identification_type: Optional[IdentificationType] = Field(default=None, alias="identificationType")
    is_pep: Optional[IsPep] = Field(default=None, alias="isPep")
    job_title: Optional[BeneficialOwnerJobTitle] = Field(default=None, alias="jobTitle")
    last_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = Field(
        default=None, alias="lastName"
    )
    other_job_title: Optional[StrictStr] = Field(default=None, alias="otherJobTitle")
    percent_ownership: Optional[Annotated[float, Field(multiple_of=0.01)]] = Field(
        default=None, alias="percentOwnership"
    )
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    region: Optional[StrictStr] = None
    social_profile_links: Optional[List[Annotated[str, Field(min_length=1, strict=True, max_length=299)]]] = Field(
        default=None, alias="socialProfileLinks"
    )
    state: Optional[StrictStr] = None
