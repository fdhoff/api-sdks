# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class ApiV1ArCustomerAddress(ApiModel):
    """ApiV1ArCustomerAddress model."""

    address1: Annotated[str, Field(min_length=1, strict=True, max_length=299)]
    address2: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = None
    city: Annotated[str, Field(min_length=1, strict=True, max_length=299)]
    country: StrictStr
    postal_code: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="postalCode")
    region: StrictStr
