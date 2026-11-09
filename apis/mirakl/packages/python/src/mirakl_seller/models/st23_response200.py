# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st23_response200_shipment_errors import ST23Response200ShipmentErrors
from mirakl_seller.models.st23_response200_shipment_success import ST23Response200ShipmentSuccess
from mirakl_seller._runtime import ApiModel


class ST23Response200(ApiModel):
    """ST23Response200 model."""

    shipment_errors: Optional[List[ST23Response200ShipmentErrors]] = None
    shipment_success: Optional[List[ST23Response200ShipmentSuccess]] = None
