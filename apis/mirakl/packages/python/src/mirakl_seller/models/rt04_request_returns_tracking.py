# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class RT04RequestReturnsTracking(ApiModel):
    """RT04RequestReturnsTracking model."""

    carrier_code: Optional[StrictStr] = None
    carrier_name: Optional[StrictStr] = None
    carrier_standard_code: Optional[StrictStr] = None
    tracking_number: Optional[StrictStr] = None
    tracking_url: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
