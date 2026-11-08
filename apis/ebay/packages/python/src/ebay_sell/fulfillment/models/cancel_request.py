# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CancelRequest(ApiModel):
    """CancelRequest model."""

    cancel_completed_date: Optional[StrictStr] = Field(default=None, alias="cancelCompletedDate")
    cancel_initiator: Optional[StrictStr] = Field(default=None, alias="cancelInitiator")
    cancel_reason: Optional[StrictStr] = Field(default=None, alias="cancelReason")
    cancel_requested_date: Optional[StrictStr] = Field(default=None, alias="cancelRequestedDate")
    cancel_request_id: Optional[StrictStr] = Field(default=None, alias="cancelRequestId")
    cancel_request_state: Optional[StrictStr] = Field(default=None, alias="cancelRequestState")
