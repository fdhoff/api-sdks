# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.identity.models.business_account import BusinessAccount
from ebay_sell.identity.models.individual_account import IndividualAccount
from ebay_sell._runtime import ApiModel


class UserResponse(ApiModel):
    """UserResponse model."""

    account_type: Optional[StrictStr] = Field(default=None, alias="accountType")
    business_account: Optional[BusinessAccount] = Field(default=None, alias="businessAccount")
    individual_account: Optional[IndividualAccount] = Field(default=None, alias="individualAccount")
    registration_marketplace_id: Optional[StrictStr] = Field(default=None, alias="registrationMarketplaceId")
    status: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    username: Optional[StrictStr] = None
