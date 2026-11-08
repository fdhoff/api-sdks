# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class ReturnPolicyDetails(ApiModel):
    """ReturnPolicyDetails model."""

    policy_description_enabled: Optional[StrictBool] = Field(default=None, alias="policyDescriptionEnabled")
    refund_methods: Optional[List[StrictStr]] = Field(default=None, alias="refundMethods")
    return_methods: Optional[List[StrictStr]] = Field(default=None, alias="returnMethods")
    return_periods: Optional[List[TimeDuration]] = Field(default=None, alias="returnPeriods")
    returns_acceptance_enabled: Optional[StrictBool] = Field(default=None, alias="returnsAcceptanceEnabled")
    return_shipping_cost_payers: Optional[List[StrictStr]] = Field(default=None, alias="returnShippingCostPayers")
