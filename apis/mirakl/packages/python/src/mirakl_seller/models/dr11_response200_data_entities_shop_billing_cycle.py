# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR11Response200DataEntitiesShopBillingCycle(ApiModel):
    """DR11Response200DataEntitiesShopBillingCycle model."""

    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    id: Optional[StrictStr] = None
