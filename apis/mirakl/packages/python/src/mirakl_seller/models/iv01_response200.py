# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.iv01_response200_invoices import IV01Response200Invoices
from mirakl_seller._runtime import ApiModel


class IV01Response200(ApiModel):
    """IV01Response200 model."""

    invoices: Optional[List[IV01Response200Invoices]] = None
    total_count: Optional[StrictInt] = None
