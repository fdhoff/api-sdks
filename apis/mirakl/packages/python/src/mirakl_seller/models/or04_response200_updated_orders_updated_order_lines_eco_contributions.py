# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions(ApiModel):
    """OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions model."""

    epr_category_code: Optional[StrictStr] = None
    producer_id: Optional[StrictStr] = None
    producer_id_owner: Optional[StrictStr] = None
    total_amount: Optional[float] = None
    unit_amount: Optional[float] = None
