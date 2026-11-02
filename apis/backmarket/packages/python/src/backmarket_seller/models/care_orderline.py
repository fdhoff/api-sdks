# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.care_order import CareOrder
from backmarket_seller.models.snapshot import Snapshot
from backmarket_seller._runtime import ApiModel


class CareOrderline(ApiModel):
    """CareOrderline model."""

    id: Optional[StrictInt] = None
    order: Optional[CareOrder] = None
    snapshot: Optional[Snapshot] = None
    quantity: Optional[StrictInt] = None
    price: Optional[StrictStr] = None
    state: Optional[StrictInt] = None
    trust_pack_plus: Optional[StrictBool] = None
