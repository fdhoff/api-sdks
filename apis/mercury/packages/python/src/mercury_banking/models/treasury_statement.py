# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking.models.treasury_statement_document_type import TreasuryStatementDocumentType
from mercury_banking._runtime import ApiModel


class TreasuryStatement(ApiModel):
    """TreasuryStatement model."""

    account_id: UUID = Field(alias="accountId")
    created_at: StrictStr = Field(alias="createdAt")
    creation_date: StrictStr = Field(alias="creationDate")
    description: StrictStr
    document_type: TreasuryStatementDocumentType = Field(alias="documentType")
    download_url: StrictStr = Field(alias="downloadUrl")
    id: UUID
    period_end: date = Field(alias="periodEnd")
    period_start: date = Field(alias="periodStart")
    updated_at: StrictStr = Field(alias="updatedAt")
