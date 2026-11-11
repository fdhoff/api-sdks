# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.auto_transfer_rules_response_page import AutoTransferRulesResponsePage
from mercury_banking.models.user_task import UserTask
from mercury_banking._runtime import ApiModel


class TasksResponse(ApiModel):
    """TasksResponse model."""

    page: AutoTransferRulesResponsePage
    tasks: List[UserTask]
