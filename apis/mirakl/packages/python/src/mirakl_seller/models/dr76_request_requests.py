# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR76RequestRequests(ApiModel):
    """DR76RequestRequests model."""

    due_date: Optional[datetime] = None
    issue_date: Optional[datetime] = None
    request_id: StrictStr
    total_amount_excluding_taxes: Optional[float] = None
    total_tax_amount: Optional[float] = None
