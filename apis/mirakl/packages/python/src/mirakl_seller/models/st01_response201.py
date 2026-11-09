# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st01_response201_shipment_errors import ST01Response201ShipmentErrors
from mirakl_seller.models.st01_response201_shipment_success import ST01Response201ShipmentSuccess
from mirakl_seller._runtime import ApiModel


class ST01Response201(ApiModel):
    """ST01Response201 model."""

    shipment_errors: List[ST01Response201ShipmentErrors]
    shipment_success: List[ST01Response201ShipmentSuccess]
