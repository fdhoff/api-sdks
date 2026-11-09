# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class S30Response200ShopDocuments(ApiModel):
    """S30Response200ShopDocuments model."""

    date_uploaded: Optional[datetime] = None
    file_name: StrictStr
    id: StrictInt
    type: StrictStr
