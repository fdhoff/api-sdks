# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.address import Address
from ebay_sell.fulfillment.models.phone_number import PhoneNumber
from ebay_sell._runtime import ApiModel


class ExtendedContact(ApiModel):
    """ExtendedContact model."""

    company_name: Optional[StrictStr] = Field(default=None, alias="companyName")
    contact_address: Optional[Address] = Field(default=None, alias="contactAddress")
    email: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    primary_phone: Optional[PhoneNumber] = Field(default=None, alias="primaryPhone")
