# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OF22Response200AllPricesContext(ApiModel):
    """OF22Response200AllPricesContext model."""

    channel_codes: Optional[List[StrictStr]] = None
    customer_group_ids: Optional[List[StrictStr]] = None
    customer_organization_ids: Optional[List[StrictStr]] = None
    end_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
