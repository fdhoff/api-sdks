# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.card_budget import CardBudget
from mercury_banking.models.card_expiration import CardExpiration
from mercury_banking.models.card_kind import CardKind
from mercury_banking.models.card_status import CardStatus
from mercury_banking.models.card_type import CardType
from mercury_banking.models.merchant_info import MerchantInfo
from mercury_banking.models.mercury_category import MercuryCategory
from mercury_banking.models.physical_card_status import PhysicalCardStatus
from mercury_banking.models.spend_limit import SpendLimit
from mercury_banking.models.spend_limit_type import SpendLimitType
from mercury_banking._runtime import ApiModel


class Card(ApiModel):
    """Card model."""

    account_id: StrictStr = Field(alias="accountId")
    budgets: List[CardBudget]
    category_locks: List[MercuryCategory] = Field(alias="categoryLocks")
    created_at: StrictStr = Field(alias="createdAt")
    expiration: CardExpiration
    id: UUID
    is_agent_card: StrictBool = Field(alias="isAgentCard")
    is_single_use: StrictBool = Field(alias="isSingleUse")
    kind: CardKind
    last_four: StrictStr = Field(alias="lastFour")
    merchant_lock: Optional[MerchantInfo] = Field(default=None, alias="merchantLock")
    name_on_card: StrictStr = Field(alias="nameOnCard")
    nickname: Optional[StrictStr] = None
    physical_card_status: Optional[PhysicalCardStatus] = Field(default=None, alias="physicalCardStatus")
    spend_limit: Optional[SpendLimit] = Field(default=None, alias="spendLimit")
    spend_limit_type: SpendLimitType = Field(alias="spendLimitType")
    status: CardStatus
    type: CardType
    updated_at: StrictStr = Field(alias="updatedAt")
    user_id: StrictStr = Field(alias="userId")
