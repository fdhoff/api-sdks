# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.care_client import CareClient
from backmarket_seller.models.care_orderline import CareOrderline
from backmarket_seller.models.claim import Claim
from backmarket_seller.models.message import Message
from backmarket_seller.models.seller import Seller
from backmarket_seller._runtime import ApiModel


class GetCareFolderDetailsResponse(ApiModel):
    """GetCareFolderDetailsResponse model."""

    backcare: Optional[StrictBool] = None
    client: Optional[CareClient] = None
    country_code: Optional[StrictStr] = None
    date_closed: Optional[datetime] = None
    date_creation: Optional[datetime] = None
    date_last_message: Optional[datetime] = None
    date_modification: Optional[datetime] = None
    id: Optional[StrictInt] = None
    lines: Optional[List[Claim]] = None
    merchant: Optional[Seller] = None
    messages: Optional[List[Message]] = None
    orderline: Optional[CareOrderline] = None
    state: Optional[StrictInt] = None
