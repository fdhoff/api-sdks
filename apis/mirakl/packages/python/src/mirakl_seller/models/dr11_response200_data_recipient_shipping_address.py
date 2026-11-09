# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR11Response200DataRecipientShippingAddress(ApiModel):
    """DR11Response200DataRecipientShippingAddress model."""

    city: StrictStr
    civility: Optional[StrictStr] = None
    company: Optional[StrictStr] = None
    company_2: Optional[StrictStr] = None
    country: StrictStr
    country_iso_code: Optional[StrictStr] = None
    firstname: Optional[StrictStr] = None
    lastname: StrictStr
    state: Optional[StrictStr] = None
    street_1: StrictStr
    street_2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
