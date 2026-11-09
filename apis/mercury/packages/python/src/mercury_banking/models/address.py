# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class Address(ApiModel):
    """Address model."""

    address1: StrictStr
    address2: Optional[StrictStr] = None
    city: StrictStr
    country: StrictStr
    name: StrictStr
    postal_code: StrictStr = Field(alias="postalCode")
    region: StrictStr
