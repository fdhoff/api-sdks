# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking.models.books_api_instance_relationship import BooksAPIInstanceRelationship
from mercury_banking._runtime import ApiModel


class BooksAPIInstance(ApiModel):
    """BooksAPIInstance model."""

    books_id: UUID = Field(alias="booksId")
    callsign: StrictStr
    company_name: StrictStr = Field(alias="companyName")
    organization_id: UUID = Field(alias="organizationId")
    relationship: BooksAPIInstanceRelationship
