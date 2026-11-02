# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class CareAddress(ApiModel):
    """CareAddress model."""

    company: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    street: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    customer_id_number: Optional[StrictStr] = None
