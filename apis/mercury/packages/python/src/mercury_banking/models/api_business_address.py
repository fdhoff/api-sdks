# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class APIBusinessAddress(ApiModel):
    """APIBusinessAddress model."""

    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    region: Optional[StrictStr] = None
