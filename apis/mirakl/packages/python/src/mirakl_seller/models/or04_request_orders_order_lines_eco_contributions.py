# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR04RequestOrdersOrderLinesEcoContributions(ApiModel):
    """OR04RequestOrdersOrderLinesEcoContributions model."""

    epr_category_code: StrictStr
    producer_id: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    unit_amount: Optional[Annotated[float, Field(le=100000000000000000, ge=0)]] = None
