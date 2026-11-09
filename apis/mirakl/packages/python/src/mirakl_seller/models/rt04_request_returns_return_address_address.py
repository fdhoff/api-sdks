# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class RT04RequestReturnsReturnAddressAddress(ApiModel):
    """RT04RequestReturnsReturnAddressAddress model."""

    city: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    country_iso_code: StrictStr
    state: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    street1: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    street2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    zip_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
