# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PaymentsProgramResponse(ApiModel):
    """PaymentsProgramResponse model."""

    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    payments_program_type: Optional[StrictStr] = Field(default=None, alias="paymentsProgramType")
    status: Optional[StrictStr] = None
    was_previously_opted_in: Optional[StrictBool] = Field(default=None, alias="wasPreviouslyOptedIn")
