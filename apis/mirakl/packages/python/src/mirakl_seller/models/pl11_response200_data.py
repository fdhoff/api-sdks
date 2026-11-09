# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pl11_response200_data_order_lines import PL11Response200DataOrderLines
from mirakl_seller.models.pl11_response200_data_picklist_lines import PL11Response200DataPicklistLines
from mirakl_seller._runtime import ApiModel


class PL11Response200Data(ApiModel):
    """PL11Response200Data model."""

    date_created: datetime
    id: StrictStr
    last_updated: datetime
    order_lines: List[PL11Response200DataOrderLines]
    picklist_lines: List[PL11Response200DataPicklistLines]
    pickrun_code: Optional[StrictStr] = None
    pickup_date: datetime
    shop_id: Optional[StrictInt] = None
    state: StrictStr
