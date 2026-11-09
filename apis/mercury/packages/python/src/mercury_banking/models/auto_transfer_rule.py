# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.auto_transfer_rule_kind import AutoTransferRuleKind
from mercury_banking._runtime import ApiModel


class AutoTransferRule(ApiModel):
    """AutoTransferRule model."""

    controlled_account_id: UUID = Field(alias="controlledAccountId")
    description: StrictStr
    details: AutoTransferRuleKind
    frequency: StrictStr
    id: UUID
    is_paused: StrictBool = Field(alias="isPaused")
    name: StrictStr
    next_transfer_at: Optional[StrictStr] = Field(default=None, alias="nextTransferAt")
    nickname: Optional[StrictStr] = None
