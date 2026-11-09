# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.security_id_type import SecurityIdType
from mercury_banking._runtime import ApiModel


class TreasuryDividend(ApiModel):
    """TreasuryDividend model."""

    amount: Annotated[float, Field(multiple_of=0.01)]
    id: StrictStr
    security_name: StrictStr = Field(alias="securityName")
    type: SecurityIdType
