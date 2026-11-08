# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.category_type import CategoryType
from ebay_sell.account.models.international_return_override_type import InternationalReturnOverrideType
from ebay_sell.account.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class ReturnPolicy(ApiModel):
    """ReturnPolicy model."""

    category_types: Optional[List[CategoryType]] = Field(default=None, alias="categoryTypes")
    description: Optional[StrictStr] = None
    extended_holiday_returns_offered: Optional[StrictBool] = Field(default=None, alias="extendedHolidayReturnsOffered")
    international_override: Optional[InternationalReturnOverrideType] = Field(
        default=None, alias="internationalOverride"
    )
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    refund_method: Optional[StrictStr] = Field(default=None, alias="refundMethod")
    restocking_fee_percentage: Optional[StrictStr] = Field(default=None, alias="restockingFeePercentage")
    return_instructions: Optional[StrictStr] = Field(default=None, alias="returnInstructions")
    return_method: Optional[StrictStr] = Field(default=None, alias="returnMethod")
    return_period: Optional[TimeDuration] = Field(default=None, alias="returnPeriod")
    return_policy_id: Optional[StrictStr] = Field(default=None, alias="returnPolicyId")
    returns_accepted: Optional[StrictBool] = Field(default=None, alias="returnsAccepted")
    return_shipping_cost_payer: Optional[StrictStr] = Field(default=None, alias="returnShippingCostPayer")
