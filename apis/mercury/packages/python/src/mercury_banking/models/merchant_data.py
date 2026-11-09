# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.mercury_category import MercuryCategory
from mercury_banking._runtime import ApiModel


class MerchantData(ApiModel):
    """MerchantData model."""

    amount: Optional[Annotated[int, Field(le=9223372036854776000, strict=True, ge=-9223372036854776000)]] = None
    category: Optional[MercuryCategory] = None
    category_code: Optional[StrictStr] = Field(default=None, alias="categoryCode")
    currency: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
