# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st31_response200_shipment_update_errors import ST31Response200ShipmentUpdateErrors
from mirakl_seller.models.st31_response200_shipment_update_success import ST31Response200ShipmentUpdateSuccess
from mirakl_seller._runtime import ApiModel


class ST31Response200(ApiModel):
    """ST31Response200 model."""

    shipment_update_errors: Optional[List[ST31Response200ShipmentUpdateErrors]] = None
    shipment_update_success: Optional[List[ST31Response200ShipmentUpdateSuccess]] = None
