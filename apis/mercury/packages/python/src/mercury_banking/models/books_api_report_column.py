# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class BooksAPIReportColumn(ApiModel):
    """BooksAPIReportColumn model."""

    end_date: Optional[date] = Field(default=None, alias="endDate")
    is_partial: StrictBool = Field(alias="isPartial")
    label: StrictStr
    start_date: Optional[date] = Field(default=None, alias="startDate")
