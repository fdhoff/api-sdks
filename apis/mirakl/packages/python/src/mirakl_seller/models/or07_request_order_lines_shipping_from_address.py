# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR07RequestOrderLinesShippingFromAddress(ApiModel):
    """OR07RequestOrderLinesShippingFromAddress model."""

    city: Optional[StrictStr] = None
    country_iso_code: StrictStr
    state: Optional[StrictStr] = None
    street_1: Optional[StrictStr] = None
    street_2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
