# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.auto_transfer_rule_kind_distribute_amount import AutoTransferRuleKindDistributeAmount
from mercury_banking.models.auto_transfer_rule_kind_distribute_percentage import (
    AutoTransferRuleKindDistributePercentage,
)
from mercury_banking.models.auto_transfer_rule_kind_maintain_target_balance import (
    AutoTransferRuleKindMaintainTargetBalance,
)
from typing import Union

AutoTransferRuleKind = Union[
    AutoTransferRuleKindDistributeAmount,
    AutoTransferRuleKindDistributePercentage,
    AutoTransferRuleKindMaintainTargetBalance,
]
