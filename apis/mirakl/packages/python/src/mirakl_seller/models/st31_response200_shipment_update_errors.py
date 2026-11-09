# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st31_response200_shipment_update_errors_errors import (
    ST31Response200ShipmentUpdateErrorsErrors,
)
from mirakl_seller._runtime import ApiModel


class ST31Response200ShipmentUpdateErrors(ApiModel):
    """ST31Response200ShipmentUpdateErrors model."""

    errors: Optional[List[ST31Response200ShipmentUpdateErrorsErrors]] = None
    shipment_id: Optional[StrictStr] = None
