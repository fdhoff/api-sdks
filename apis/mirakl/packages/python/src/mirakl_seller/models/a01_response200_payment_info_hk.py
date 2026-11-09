# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.a01_response200_payment_info import A01Response200PaymentInfo
from mirakl_seller._runtime import ApiModel


class A01Response200PaymentInfoHk(A01Response200PaymentInfo):
    """A01Response200PaymentInfoHk model."""

    bank_account_number: Annotated[str, Field(min_length=9, strict=True, max_length=12)]
    bank_city: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]] = None
    bank_name: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    bank_street: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]] = None
    bank_zip: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    swift_code: StrictStr
