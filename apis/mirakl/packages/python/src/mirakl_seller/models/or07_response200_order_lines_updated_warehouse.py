# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR07Response200OrderLinesUpdatedWarehouse(ApiModel):
    """OR07Response200OrderLinesUpdatedWarehouse model."""

    code: Optional[StrictStr] = None
