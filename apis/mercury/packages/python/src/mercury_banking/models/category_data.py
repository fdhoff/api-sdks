# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking._runtime import ApiModel


class CategoryData(ApiModel):
    """CategoryData model."""

    id: UUID
    name: StrictStr
    visible_for_card_spend: StrictBool = Field(alias="visibleForCardSpend")
    visible_for_other: StrictBool = Field(alias="visibleForOther")
    visible_for_reimbursements: StrictBool = Field(alias="visibleForReimbursements")
