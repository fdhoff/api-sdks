# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A21Response200OffersCount(ApiModel):
    """A21Response200OffersCount model."""

    period: Optional[StrictStr] = None
    value: Optional[StrictInt] = None
