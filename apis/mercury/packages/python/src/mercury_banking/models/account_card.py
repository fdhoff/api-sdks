# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.card_network import CardNetwork
from mercury_banking.models.card_status import CardStatus
from mercury_banking.models.card_type import CardType
from mercury_banking.models.physical_card_status import PhysicalCardStatus
from mercury_banking.models.spend_limit import SpendLimit
from mercury_banking._runtime import ApiModel


class AccountCard(ApiModel):
    """AccountCard model."""

    card_id: StrictStr = Field(alias="cardId")
    created_at: StrictStr = Field(alias="createdAt")
    last_four_digits: StrictStr = Field(alias="lastFourDigits")
    name_on_card: StrictStr = Field(alias="nameOnCard")
    network: CardNetwork
    physical_card_status: Optional[PhysicalCardStatus] = Field(default=None, alias="physicalCardStatus")
    spend_limit: SpendLimit = Field(alias="spendLimit")
    status: CardStatus
    type: CardType
    updated_at: StrictStr = Field(alias="updatedAt")
    user_id: StrictStr = Field(alias="userId")
