# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesRefundsEcoContributions(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesRefundsEcoContributions model."""

    epr_category_code: StrictStr
    producer_id: StrictStr
    producer_id_owner: StrictStr
    total_amount: Optional[float] = None
    unit_amount: Optional[float] = None
