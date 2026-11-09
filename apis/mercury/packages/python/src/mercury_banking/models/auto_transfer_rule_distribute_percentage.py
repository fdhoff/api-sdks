# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.auto_transfer_rule_reservoir_percentage import AutoTransferRuleReservoirPercentage
from mercury_banking._runtime import ApiModel


class AutoTransferRuleDistributePercentage(ApiModel):
    """AutoTransferRuleDistributePercentage model."""

    reservoir_accounts: List[AutoTransferRuleReservoirPercentage] = Field(alias="reservoirAccounts")
