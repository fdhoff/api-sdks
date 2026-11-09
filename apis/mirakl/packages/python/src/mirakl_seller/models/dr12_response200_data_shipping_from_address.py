# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR12Response200DataShippingFromAddress(ApiModel):
    """DR12Response200DataShippingFromAddress model."""

    city: Optional[StrictStr] = None
    country_iso_code: StrictStr
    state: Optional[StrictStr] = None
    street1: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
