# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_shipment_additional_information import (
    ST01Response201ShipmentSuccessShipmentAdditionalInformation,
)
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessShipmentAdditionalInformationString(
    ST01Response201ShipmentSuccessShipmentAdditionalInformation
):
    """ST01Response201ShipmentSuccessShipmentAdditionalInformationString model."""

    value: Optional[StrictStr] = None
