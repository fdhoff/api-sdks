# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a02_response200_updated_default_billing_information_corporate_information import (
    A02Response200UpdatedDefaultBillingInformationCorporateInformation,
)
from mirakl_seller.models.a02_response200_updated_default_billing_information_fiscal_information import (
    A02Response200UpdatedDefaultBillingInformationFiscalInformation,
)
from mirakl_seller.models.a02_response200_updated_default_billing_information_fiscal_representative import (
    A02Response200UpdatedDefaultBillingInformationFiscalRepresentative,
)
from mirakl_seller.models.a02_response200_updated_default_billing_information_personal_information import (
    A02Response200UpdatedDefaultBillingInformationPersonalInformation,
)
from mirakl_seller.models.a02_response200_updated_default_billing_information_registration_address import (
    A02Response200UpdatedDefaultBillingInformationRegistrationAddress,
)
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedDefaultBillingInformation(ApiModel):
    """A02Response200UpdatedDefaultBillingInformation model."""

    corporate_information: Optional[A02Response200UpdatedDefaultBillingInformationCorporateInformation] = None
    default_language: StrictStr
    fiscal_information: Optional[A02Response200UpdatedDefaultBillingInformationFiscalInformation] = None
    fiscal_representative: Optional[A02Response200UpdatedDefaultBillingInformationFiscalRepresentative] = None
    id: StrictStr
    personal_information: Optional[A02Response200UpdatedDefaultBillingInformationPersonalInformation] = None
    registration_address: A02Response200UpdatedDefaultBillingInformationRegistrationAddress
