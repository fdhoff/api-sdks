# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_external_party_id import BooksExternalPartyId
from mercury_banking._runtime import ApiModel


class BooksLineEntryPaymentApplicationAccrualSource(ApiModel):
    """BooksLineEntryPaymentApplicationAccrualSource model."""

    accrual_source_id: StrictStr = Field(alias="accrualSourceId")
    effective_date: date = Field(alias="effectiveDate")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    external_party_id: Optional[BooksExternalPartyId] = Field(default=None, alias="externalPartyId")
    gross_amount: float = Field(alias="grossAmount")
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    type: StrictStr
