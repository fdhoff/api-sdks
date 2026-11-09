# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.accounting_sync_status import AccountingSyncStatus
from mercury_banking._runtime import ApiModel


class TransactionAccountingStatus(ApiModel):
    """TransactionAccountingStatus model."""

    errored_at: Optional[StrictStr] = Field(default=None, alias="erroredAt")
    excluded_at: Optional[StrictStr] = Field(default=None, alias="excludedAt")
    reviewed_at: Optional[StrictStr] = Field(default=None, alias="reviewedAt")
    status: AccountingSyncStatus
    sync_started_at: Optional[StrictStr] = Field(default=None, alias="syncStartedAt")
    synced_at: Optional[StrictStr] = Field(default=None, alias="syncedAt")
