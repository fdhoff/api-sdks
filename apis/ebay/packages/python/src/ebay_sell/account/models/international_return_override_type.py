# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class InternationalReturnOverrideType(ApiModel):
    """InternationalReturnOverrideType model."""

    return_method: Optional[StrictStr] = Field(default=None, alias="returnMethod")
    return_period: Optional[TimeDuration] = Field(default=None, alias="returnPeriod")
    returns_accepted: Optional[StrictBool] = Field(default=None, alias="returnsAccepted")
    return_shipping_cost_payer: Optional[StrictStr] = Field(default=None, alias="returnShippingCostPayer")
