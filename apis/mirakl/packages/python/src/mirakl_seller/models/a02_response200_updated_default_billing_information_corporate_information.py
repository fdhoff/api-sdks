# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a02_response200_updated_default_billing_information_corporate_information_complementary_information import (
    A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation,
)
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedDefaultBillingInformationCorporateInformation(ApiModel):
    """A02Response200UpdatedDefaultBillingInformationCorporateInformation model."""

    company_registration_name: Optional[StrictStr] = None
    company_registration_number: Optional[StrictStr] = None
    complementary_information: Optional[
        A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation
    ] = None
    electronic_address: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
