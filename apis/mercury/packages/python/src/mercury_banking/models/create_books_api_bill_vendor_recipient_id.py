# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking._runtime import ApiModel


class CreateBooksAPIBillVendorRecipientId(ApiModel):
    """CreateBooksAPIBillVendorRecipientId model."""

    contents: UUID
    tag: StrictStr
