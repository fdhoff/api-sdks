# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_recipient_organization_address import (
    DR11Response200DataRecipientOrganizationAddress,
)
from mirakl_seller._runtime import ApiModel


class DR11Response200DataRecipientOrganization(ApiModel):
    """DR11Response200DataRecipientOrganization model."""

    address: Optional[DR11Response200DataRecipientOrganizationAddress] = None
    business_activity_code: Optional[StrictStr] = None
    company_shareholders: Optional[StrictStr] = None
    electronic_address: Optional[StrictStr] = None
    identification_number: Optional[StrictStr] = None
    is_in_liquidation: Optional[StrictBool] = None
    legal_form: Optional[StrictStr] = None
    local_tax_number: Optional[StrictStr] = None
    local_tax_number_country: Optional[StrictStr] = None
    name: StrictStr
    organization_id: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
    share_capital: Optional[float] = None
    share_capital_currency: Optional[StrictStr] = None
    tax_identification_number: Optional[StrictStr] = None
    tax_number_country: Optional[StrictStr] = None
    trade_company_registration_location: Optional[StrictStr] = None
