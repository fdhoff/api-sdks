# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class Address(ApiModel):
    """Address model."""

    id: Optional[StrictInt] = None
    country: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    company: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    state: Optional[StrictStr] = None
    street: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
