# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st31_request_shipments_shipment_additional_information import (
    ST31RequestShipmentsShipmentAdditionalInformation,
)
from mirakl_seller._runtime import ApiModel


class ST31RequestShipmentsShipmentAdditionalInformationDate(ST31RequestShipmentsShipmentAdditionalInformation):
    """ST31RequestShipmentsShipmentAdditionalInformationDate model."""

    value: StrictStr
