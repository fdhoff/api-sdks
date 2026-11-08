# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.identity.models.address import Address
from ebay_sell.identity.models.phone import Phone
from ebay_sell._runtime import ApiModel


class IndividualAccount(ApiModel):
    """IndividualAccount model."""

    email: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    primary_phone: Optional[Phone] = Field(default=None, alias="primaryPhone")
    registration_address: Optional[Address] = Field(default=None, alias="registrationAddress")
    secondary_phone: Optional[Phone] = Field(default=None, alias="secondaryPhone")
