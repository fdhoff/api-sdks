# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.auto_transfer_rule_reservoir_amount import AutoTransferRuleReservoirAmount
from mercury_banking._runtime import ApiModel


class AutoTransferRuleDistributeAmount(ApiModel):
    """AutoTransferRuleDistributeAmount model."""

    reservoir_accounts: List[AutoTransferRuleReservoirAmount] = Field(alias="reservoirAccounts")
