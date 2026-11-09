# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A01Response200ContactInformations(ApiModel):
    """A01Response200ContactInformations model."""

    city: StrictStr
    civility: Optional[StrictStr] = None
    country: StrictStr
    email: StrictStr
    fax: Optional[StrictStr] = None
    firstname: Optional[StrictStr] = None
    lastname: StrictStr
    phone: Optional[StrictStr] = None
    phone_secondary: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    street1: StrictStr
    street2: Optional[StrictStr] = None
    web_site: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
