# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_shipment_additional_information import (
    ST11Response200DataShipmentAdditionalInformation,
)
from mirakl_seller._runtime import ApiModel


class ST11Response200DataShipmentAdditionalInformationDate(ST11Response200DataShipmentAdditionalInformation):
    """ST11Response200DataShipmentAdditionalInformationDate model."""

    value: Optional[StrictStr] = None
