# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.card_configuration import CardConfiguration
from mercury_banking.models.card_kind import CardKind
from mercury_banking.models.create_card_type import CreateCardType
from mercury_banking.models.create_spend_limit import CreateSpendLimit
from mercury_banking._runtime import ApiModel


class CreateCardRequest(ApiModel):
    """CreateCardRequest model."""

    account_id: Optional[UUID] = Field(default=None, alias="accountId")
    card_configuration: Optional[CardConfiguration] = Field(default=None, alias="cardConfiguration")
    kind: CardKind
    nickname: Optional[StrictStr] = None
    spend_limit: Optional[CreateSpendLimit] = Field(default=None, alias="spendLimit")
    type: CreateCardType
    user_id: UUID = Field(alias="userId")
