# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A01Response200DefaultBillingInformationCorporateInformationComplementaryInformation(ApiModel):
    """A01Response200DefaultBillingInformationCorporateInformationComplementaryInformation model."""

    business_activity_code: Optional[StrictStr] = None
    company_registration_city: Optional[StrictStr] = None
    company_registration_province: Optional[StrictStr] = None
    company_shareholders: Optional[StrictStr] = None
    is_in_liquidation: Optional[StrictBool] = None
    legal_form: Optional[StrictStr] = None
    share_capital: Optional[float] = None
    share_capital_currency: Optional[StrictStr] = None
    sole_trader: Optional[StrictBool] = None
