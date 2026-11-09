# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a01_response200_specific_billing_informations_corporate_information import (
    A01Response200SpecificBillingInformationsCorporateInformation,
)
from mirakl_seller.models.a01_response200_specific_billing_informations_fiscal_information import (
    A01Response200SpecificBillingInformationsFiscalInformation,
)
from mirakl_seller.models.a01_response200_specific_billing_informations_fiscal_representative import (
    A01Response200SpecificBillingInformationsFiscalRepresentative,
)
from mirakl_seller.models.a01_response200_specific_billing_informations_personal_information import (
    A01Response200SpecificBillingInformationsPersonalInformation,
)
from mirakl_seller.models.a01_response200_specific_billing_informations_registration_address import (
    A01Response200SpecificBillingInformationsRegistrationAddress,
)
from mirakl_seller._runtime import ApiModel


class A01Response200SpecificBillingInformations(ApiModel):
    """A01Response200SpecificBillingInformations model."""

    corporate_information: Optional[A01Response200SpecificBillingInformationsCorporateInformation] = None
    fiscal_information: Optional[A01Response200SpecificBillingInformationsFiscalInformation] = None
    fiscal_representative: Optional[A01Response200SpecificBillingInformationsFiscalRepresentative] = None
    id: StrictStr
    personal_information: Optional[A01Response200SpecificBillingInformationsPersonalInformation] = None
    registration_address: A01Response200SpecificBillingInformationsRegistrationAddress
