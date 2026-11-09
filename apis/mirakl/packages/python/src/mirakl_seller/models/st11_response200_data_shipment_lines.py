# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class ST11Response200DataShipmentLines(ApiModel):
    """ST11Response200DataShipmentLines model."""

    offer_sku: Optional[StrictStr] = None
    order_line_id: Optional[StrictStr] = None
    package_reference: Optional[StrictStr] = None
    quantity: Annotated[int, Field(strict=True, ge=1)]
