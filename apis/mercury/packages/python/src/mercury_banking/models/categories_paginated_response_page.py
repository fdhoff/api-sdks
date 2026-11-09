# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking._runtime import ApiModel


class CategoriesPaginatedResponsePage(ApiModel):
    """CategoriesPaginatedResponsePage model."""

    next_page: Optional[UUID] = Field(default=None, alias="nextPage")
    previous_page: Optional[UUID] = Field(default=None, alias="previousPage")
