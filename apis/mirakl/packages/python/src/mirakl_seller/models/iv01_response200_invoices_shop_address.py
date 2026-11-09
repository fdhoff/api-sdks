# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class IV01Response200InvoicesShopAddress(ApiModel):
    """IV01Response200InvoicesShopAddress model."""

    city: Optional[StrictStr] = None
    civility: Optional[StrictStr] = None
    company: Optional[StrictStr] = None
    complementary: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    firstname: Optional[StrictStr] = None
    lastname: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    phone_secondary: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    street1: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
