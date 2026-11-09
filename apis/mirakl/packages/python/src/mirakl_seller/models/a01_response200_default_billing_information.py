# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a01_response200_default_billing_information_corporate_information import (
    A01Response200DefaultBillingInformationCorporateInformation,
)
from mirakl_seller.models.a01_response200_default_billing_information_fiscal_information import (
    A01Response200DefaultBillingInformationFiscalInformation,
)
from mirakl_seller.models.a01_response200_default_billing_information_fiscal_representative import (
    A01Response200DefaultBillingInformationFiscalRepresentative,
)
from mirakl_seller.models.a01_response200_default_billing_information_personal_information import (
    A01Response200DefaultBillingInformationPersonalInformation,
)
from mirakl_seller.models.a01_response200_default_billing_information_registration_address import (
    A01Response200DefaultBillingInformationRegistrationAddress,
)
from mirakl_seller._runtime import ApiModel


class A01Response200DefaultBillingInformation(ApiModel):
    """A01Response200DefaultBillingInformation model."""

    corporate_information: Optional[A01Response200DefaultBillingInformationCorporateInformation] = None
    default_language: StrictStr
    fiscal_information: Optional[A01Response200DefaultBillingInformationFiscalInformation] = None
    fiscal_representative: Optional[A01Response200DefaultBillingInformationFiscalRepresentative] = None
    id: StrictStr
    personal_information: Optional[A01Response200DefaultBillingInformationPersonalInformation] = None
    registration_address: A01Response200DefaultBillingInformationRegistrationAddress
