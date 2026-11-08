# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CouponConfiguration(ApiModel):
    """CouponConfiguration model."""

    coupon_code: Optional[StrictStr] = Field(default=None, alias="couponCode")
    coupon_type: Optional[StrictStr] = Field(default=None, alias="couponType")
    max_coupon_redemption_per_user: Optional[StrictInt] = Field(default=None, alias="maxCouponRedemptionPerUser")
