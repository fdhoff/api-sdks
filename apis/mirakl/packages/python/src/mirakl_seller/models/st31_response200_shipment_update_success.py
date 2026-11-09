# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st31_response200_shipment_update_success_shipment_additional_information import (
    ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation,
)
from mirakl_seller._runtime import ApiModel


class ST31Response200ShipmentUpdateSuccess(ApiModel):
    """ST31Response200ShipmentUpdateSuccess model."""

    shipment_additional_information: Optional[
        List[ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation]
    ] = None
    shipment_id: Optional[StrictStr] = None
