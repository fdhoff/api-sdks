# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class SBC11Response200DataPayOut(ApiModel):
    """SBC11Response200DataPayOut model."""

    failure_reason: Optional[StrictStr] = None
    reference: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    transaction_date: Optional[datetime] = None
