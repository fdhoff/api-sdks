# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.api_application_type import APIApplicationType
from mercury_banking.models.api_beneficial_owner import APIBeneficialOwner
from mercury_banking.models.api_business_address import APIBusinessAddress
from mercury_banking.models.api_business_contact_details import APIBusinessContactDetails
from mercury_banking.models.api_formation_details import APIFormationDetails
from mercury_banking.models.api_onboarding_data_about import APIOnboardingDataAbout
from mercury_banking._runtime import ApiModel


class APISubmitOnboardingDataParams(ApiModel):
    """APISubmitOnboardingDataParams model."""

    about: Optional[APIOnboardingDataAbout] = None
    application_type: Optional[APIApplicationType] = Field(default=None, alias="applicationType")
    beneficial_owners: Annotated[List[APIBeneficialOwner], Field(min_length=1)] = Field(alias="beneficialOwners")
    business_contact_details: Optional[APIBusinessContactDetails] = Field(default=None, alias="businessContactDetails")
    business_legal_address: Optional[APIBusinessAddress] = Field(default=None, alias="businessLegalAddress")
    business_physical_address: Optional[APIBusinessAddress] = Field(default=None, alias="businessPhysicalAddress")
    formation_details: Optional[APIFormationDetails] = Field(default=None, alias="formationDetails")
    invite_email: Optional[StrictStr] = Field(default=None, alias="inviteEmail")
    partner: StrictStr
    webhook_url: Optional[StrictStr] = Field(default=None, alias="webhookURL")
