# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a02_response200_updated_specific_billing_informations_corporate_information import (
    A02Response200UpdatedSpecificBillingInformationsCorporateInformation,
)
from mirakl_seller.models.a02_response200_updated_specific_billing_informations_fiscal_information import (
    A02Response200UpdatedSpecificBillingInformationsFiscalInformation,
)
from mirakl_seller.models.a02_response200_updated_specific_billing_informations_fiscal_representative import (
    A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative,
)
from mirakl_seller.models.a02_response200_updated_specific_billing_informations_personal_information import (
    A02Response200UpdatedSpecificBillingInformationsPersonalInformation,
)
from mirakl_seller.models.a02_response200_updated_specific_billing_informations_registration_address import (
    A02Response200UpdatedSpecificBillingInformationsRegistrationAddress,
)
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedSpecificBillingInformations(ApiModel):
    """A02Response200UpdatedSpecificBillingInformations model."""

    corporate_information: Optional[A02Response200UpdatedSpecificBillingInformationsCorporateInformation] = None
    fiscal_information: Optional[A02Response200UpdatedSpecificBillingInformationsFiscalInformation] = None
    fiscal_representative: Optional[A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative] = None
    id: StrictStr
    personal_information: Optional[A02Response200UpdatedSpecificBillingInformationsPersonalInformation] = None
    registration_address: A02Response200UpdatedSpecificBillingInformationsRegistrationAddress
