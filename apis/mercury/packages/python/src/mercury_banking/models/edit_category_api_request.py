# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class EditCategoryApiRequest(ApiModel):
    """EditCategoryApiRequest model."""

    name: Optional[StrictStr] = None
    visible_for_card_spend: Optional[StrictBool] = Field(default=None, alias="visibleForCardSpend")
    visible_for_other: Optional[StrictBool] = Field(default=None, alias="visibleForOther")
    visible_for_reimbursements: Optional[StrictBool] = Field(default=None, alias="visibleForReimbursements")
