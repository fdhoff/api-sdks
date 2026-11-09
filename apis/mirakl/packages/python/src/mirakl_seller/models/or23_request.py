# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR23Request(ApiModel):
    """OR23Request model."""

    carrier_code: Optional[StrictStr] = None
    carrier_name: Optional[StrictStr] = None
    carrier_standard_code: Optional[StrictStr] = None
    carrier_url: Optional[StrictStr] = None
    tracking_number: Optional[StrictStr] = None
