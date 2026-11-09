# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.rt04_request_returns_return_address import RT04RequestReturnsReturnAddress
from mirakl_seller.models.rt04_request_returns_tracking import RT04RequestReturnsTracking
from mirakl_seller._runtime import ApiModel


class RT04RequestReturns(ApiModel):
    """RT04RequestReturns model."""

    id: StrictStr
    label_url: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    method_code: Optional[StrictStr] = None
    return_address: Optional[RT04RequestReturnsReturnAddress] = None
    rma: Optional[StrictStr] = None
    tracking: Optional[RT04RequestReturnsTracking] = None
