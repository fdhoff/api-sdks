# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.transfer_money_approval_request_response import TransferMoneyApprovalRequestResponse
from mercury_banking.models.transfer_money_approval_requests_paginated_response_page import (
    TransferMoneyApprovalRequestsPaginatedResponsePage,
)
from mercury_banking._runtime import ApiModel


class TransferMoneyApprovalRequestsPaginatedResponse(ApiModel):
    """TransferMoneyApprovalRequestsPaginatedResponse model."""

    page: TransferMoneyApprovalRequestsPaginatedResponsePage
    requests: List[TransferMoneyApprovalRequestResponse]
