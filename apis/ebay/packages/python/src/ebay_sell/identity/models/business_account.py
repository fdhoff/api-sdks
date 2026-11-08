# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.identity.models.address import Address
from ebay_sell.identity.models.contact import Contact
from ebay_sell.identity.models.phone import Phone
from ebay_sell._runtime import ApiModel


class BusinessAccount(ApiModel):
    """BusinessAccount model."""

    address: Optional[Address] = None
    doing_business_as: Optional[StrictStr] = Field(default=None, alias="doingBusinessAs")
    email: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    primary_contact: Optional[Contact] = Field(default=None, alias="primaryContact")
    primary_phone: Optional[Phone] = Field(default=None, alias="primaryPhone")
    secondary_phone: Optional[Phone] = Field(default=None, alias="secondaryPhone")
    website: Optional[StrictStr] = None
