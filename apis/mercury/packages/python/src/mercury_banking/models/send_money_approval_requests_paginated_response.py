# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.send_money_approval_request_response import SendMoneyApprovalRequestResponse
from mercury_banking.models.send_money_approval_requests_paginated_response_page import (
    SendMoneyApprovalRequestsPaginatedResponsePage,
)
from mercury_banking._runtime import ApiModel


class SendMoneyApprovalRequestsPaginatedResponse(ApiModel):
    """SendMoneyApprovalRequestsPaginatedResponse model."""

    page: SendMoneyApprovalRequestsPaginatedResponsePage
    requests: List[SendMoneyApprovalRequestResponse]
