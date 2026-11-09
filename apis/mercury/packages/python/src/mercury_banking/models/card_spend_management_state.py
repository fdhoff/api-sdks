# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.agentic_card_state import AgenticCardState
from mercury_banking._runtime import ApiModel


class CardSpendManagementState(ApiModel):
    """CardSpendManagementState model."""

    agentic_card_state: Optional[AgenticCardState] = Field(default=None, alias="agenticCardState")
    is_single_use: StrictBool = Field(alias="isSingleUse")
