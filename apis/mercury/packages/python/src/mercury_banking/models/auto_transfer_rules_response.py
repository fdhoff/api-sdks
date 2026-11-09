# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.auto_transfer_rule import AutoTransferRule
from mercury_banking.models.auto_transfer_rules_response_page import AutoTransferRulesResponsePage
from mercury_banking._runtime import ApiModel


class AutoTransferRulesResponse(ApiModel):
    """AutoTransferRulesResponse model."""

    page: AutoTransferRulesResponsePage
    rules: List[AutoTransferRule]
