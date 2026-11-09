# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st07_response200_shipment_errors import ST07Response200ShipmentErrors
from mirakl_seller.models.st07_response200_shipment_success import ST07Response200ShipmentSuccess
from mirakl_seller._runtime import ApiModel


class ST07Response200(ApiModel):
    """ST07Response200 model."""

    shipment_errors: List[ST07Response200ShipmentErrors]
    shipment_success: List[ST07Response200ShipmentSuccess]
