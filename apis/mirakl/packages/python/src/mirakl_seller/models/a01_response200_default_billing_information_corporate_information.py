# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a01_response200_default_billing_information_corporate_information_complementary_information import (
    A01Response200DefaultBillingInformationCorporateInformationComplementaryInformation,
)
from mirakl_seller._runtime import ApiModel


class A01Response200DefaultBillingInformationCorporateInformation(ApiModel):
    """A01Response200DefaultBillingInformationCorporateInformation model."""

    company_registration_name: Optional[StrictStr] = None
    company_registration_number: Optional[StrictStr] = None
    complementary_information: Optional[
        A01Response200DefaultBillingInformationCorporateInformationComplementaryInformation
    ] = None
    electronic_address: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
