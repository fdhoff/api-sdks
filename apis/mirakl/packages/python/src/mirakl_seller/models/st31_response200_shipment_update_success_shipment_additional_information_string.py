# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st31_response200_shipment_update_success_shipment_additional_information import (
    ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation,
)
from mirakl_seller._runtime import ApiModel


class ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformationString(
    ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation
):
    """ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformationString model."""

    value: StrictStr
