# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_issuer_organization_address import (
    DR11Response200DataIssuerOrganizationAddress,
)
from mirakl_seller.models.dr11_response200_data_issuer_organization_fiscal_representative import (
    DR11Response200DataIssuerOrganizationFiscalRepresentative,
)
from mirakl_seller.models.dr11_response200_data_issuer_organization_personal_information import (
    DR11Response200DataIssuerOrganizationPersonalInformation,
)
from mirakl_seller._runtime import ApiModel


class DR11Response200DataIssuerOrganization(ApiModel):
    """DR11Response200DataIssuerOrganization model."""

    address: Optional[DR11Response200DataIssuerOrganizationAddress] = None
    business_activity_code: Optional[StrictStr] = None
    company_shareholders: Optional[StrictStr] = None
    electronic_address: Optional[StrictStr] = None
    fiscal_representative: Optional[DR11Response200DataIssuerOrganizationFiscalRepresentative] = None
    identification_number: Optional[StrictStr] = None
    is_in_liquidation: Optional[StrictBool] = None
    legal_form: Optional[StrictStr] = None
    local_tax_number: Optional[StrictStr] = None
    local_tax_number_country: Optional[StrictStr] = None
    name: StrictStr
    personal_information: Optional[DR11Response200DataIssuerOrganizationPersonalInformation] = None
    phone_number: Optional[StrictStr] = None
    share_capital: Optional[float] = None
    share_capital_currency: Optional[StrictStr] = None
    sole_trader: Optional[StrictBool] = None
    tax_identification_number: Optional[StrictStr] = None
    tax_number_country: Optional[StrictStr] = None
    trade_company_registration_location: Optional[StrictStr] = None
