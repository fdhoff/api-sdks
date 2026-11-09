# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedDefaultBillingInformationFiscalRepresentative(ApiModel):
    """A02Response200UpdatedDefaultBillingInformationFiscalRepresentative model."""

    city: StrictStr
    civility: StrictStr
    company_registration_name: StrictStr
    company_registration_number: StrictStr
    country_iso_code: StrictStr
    first_name: StrictStr
    last_name: StrictStr
    local_tax_number: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    street_1: StrictStr
    street_2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
