# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.account_status import AccountStatus
from mercury_banking.models.account_type import AccountType
from mercury_banking._runtime import ApiModel


class Account(ApiModel):
    """Account model."""

    account_number: StrictStr = Field(alias="accountNumber")
    available_balance: Annotated[float, Field(multiple_of=0.01)] = Field(alias="availableBalance")
    can_receive_transactions: Optional[StrictBool] = Field(default=None, alias="canReceiveTransactions")
    can_send_real_time_payments: StrictBool = Field(alias="canSendRealTimePayments")
    created_at: StrictStr = Field(alias="createdAt")
    current_balance: Annotated[float, Field(multiple_of=0.01)] = Field(alias="currentBalance")
    dashboard_link: StrictStr = Field(alias="dashboardLink")
    id: UUID
    kind: StrictStr
    legal_business_name: StrictStr = Field(alias="legalBusinessName")
    name: StrictStr
    nickname: Optional[StrictStr] = None
    routing_number: StrictStr = Field(alias="routingNumber")
    status: AccountStatus
    type: AccountType
