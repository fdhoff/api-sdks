# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR11Response200DataPaymentTerms(ApiModel):
    """DR11Response200DataPaymentTerms model."""

    days: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
