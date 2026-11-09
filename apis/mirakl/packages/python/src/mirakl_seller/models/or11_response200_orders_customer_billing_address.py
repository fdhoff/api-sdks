# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersCustomerBillingAddress(ApiModel):
    """OR11Response200OrdersCustomerBillingAddress model."""

    city: StrictStr
    civility: Optional[StrictStr] = None
    company: Optional[StrictStr] = None
    company_2: Optional[StrictStr] = None
    country: StrictStr
    country_iso_code: StrictStr
    firstname: Optional[StrictStr] = None
    lastname: StrictStr
    phone: Optional[StrictStr] = None
    phone_secondary: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    street_1: StrictStr
    street_2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
