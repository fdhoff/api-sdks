# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class BooksAPIRetainedEarnings(ApiModel):
    """BooksAPIRetainedEarnings model."""

    calculated_current_year_earnings: List[float] = Field(alias="calculatedCurrentYearEarnings")
    calculated_retained_earnings: List[float] = Field(alias="calculatedRetainedEarnings")
