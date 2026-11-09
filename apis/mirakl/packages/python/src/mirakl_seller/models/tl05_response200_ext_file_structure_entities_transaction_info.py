# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class TL05Response200ExtFileStructureEntitiesTransactionInfo(ApiModel):
    """TL05Response200ExtFileStructureEntitiesTransactionInfo model."""

    var_date: Optional[datetime] = Field(default=None, alias="date")
    number: Optional[StrictStr] = None
