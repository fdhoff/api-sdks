# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class BooksLineEntryLinePaymentApplicationAccrualSource(ApiModel):
    """BooksLineEntryLinePaymentApplicationAccrualSource model."""

    accrual_source_id: StrictStr = Field(alias="accrualSourceId")
    end_date: date = Field(alias="endDate")
    start_date: date = Field(alias="startDate")
    type: StrictStr
