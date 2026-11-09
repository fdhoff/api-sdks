# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A01Response200BillingInfo(ApiModel):
    """A01Response200BillingInfo model."""

    bank_city: Optional[StrictStr] = None
    bank_name: Optional[StrictStr] = None
    bank_street: Optional[StrictStr] = None
    bic: Optional[StrictStr] = None
    iban: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
