# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ResponsiblePerson(ApiModel):
    """ResponsiblePerson model."""

    address_line1: Optional[StrictStr] = Field(default=None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, alias="addressLine2")
    city: Optional[StrictStr] = None
    company_name: Optional[StrictStr] = Field(default=None, alias="companyName")
    contact_url: Optional[StrictStr] = Field(default=None, alias="contactUrl")
    country: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    state_or_province: Optional[StrictStr] = Field(default=None, alias="stateOrProvince")
    types: Optional[List[StrictStr]] = None
