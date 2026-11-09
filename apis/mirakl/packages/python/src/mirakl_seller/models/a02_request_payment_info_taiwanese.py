# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.a02_request_payment_info import A02RequestPaymentInfo
from mirakl_seller._runtime import ApiModel


class A02RequestPaymentInfoTaiwanese(A02RequestPaymentInfo):
    """A02RequestPaymentInfoTaiwanese model."""

    account_number: Annotated[str, Field(min_length=8, strict=True, max_length=14)]
    bank_city: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]] = None
    bank_code: Annotated[str, Field(min_length=2, strict=True, max_length=3)]
    bank_name: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    bank_street: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100)]] = None
    bank_zip: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    branch_code: Annotated[str, Field(min_length=3, strict=True, max_length=4)]
