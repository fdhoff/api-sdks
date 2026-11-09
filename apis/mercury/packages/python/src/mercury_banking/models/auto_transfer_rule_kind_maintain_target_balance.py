# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.auto_transfer_rule_maintain_target_balance import AutoTransferRuleMaintainTargetBalance
from mercury_banking._runtime import ApiModel


class AutoTransferRuleKindMaintainTargetBalance(ApiModel):
    """AutoTransferRuleKindMaintainTargetBalance model."""

    contents: AutoTransferRuleMaintainTargetBalance
    kind: StrictStr
