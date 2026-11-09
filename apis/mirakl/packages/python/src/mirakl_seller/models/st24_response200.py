# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st24_response200_shipment_errors import ST24Response200ShipmentErrors
from mirakl_seller.models.st24_response200_shipment_success import ST24Response200ShipmentSuccess
from mirakl_seller._runtime import ApiModel


class ST24Response200(ApiModel):
    """ST24Response200 model."""

    shipment_errors: Optional[List[ST24Response200ShipmentErrors]] = None
    shipment_success: Optional[List[ST24Response200ShipmentSuccess]] = None
