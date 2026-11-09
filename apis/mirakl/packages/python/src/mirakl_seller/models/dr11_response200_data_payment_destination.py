# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from mirakl_seller._runtime import ApiModel


class DR11Response200DataPaymentDestination(ApiModel):
    """DR11Response200DataPaymentDestination model."""

    type: StrictStr = Field(alias="@type")
    payment_reference: Optional[StrictStr] = None
