# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.cancel_request import CancelRequest
from ebay_sell._runtime import ApiModel


class CancelStatus(ApiModel):
    """CancelStatus model."""

    cancelled_date: Optional[StrictStr] = Field(default=None, alias="cancelledDate")
    cancel_requests: Optional[List[CancelRequest]] = Field(default=None, alias="cancelRequests")
    cancel_state: Optional[StrictStr] = Field(default=None, alias="cancelState")
