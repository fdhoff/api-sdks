# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT01Response200ReturnSuccessReturnAddress(ApiModel):
    """RT01Response200ReturnSuccessReturnAddress model."""

    city: StrictStr
    country_iso_code: StrictStr
    state: Optional[StrictStr] = None
    street1: StrictStr
    street2: Optional[StrictStr] = None
    zip_code: StrictStr
