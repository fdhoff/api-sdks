# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedSpecificBillingInformationsPersonalInformation(ApiModel):
    """A02Response200UpdatedSpecificBillingInformationsPersonalInformation model."""

    birth_city: Optional[StrictStr] = None
    birth_country: Optional[StrictStr] = None
    birth_date: Optional[date] = None
    civility: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
