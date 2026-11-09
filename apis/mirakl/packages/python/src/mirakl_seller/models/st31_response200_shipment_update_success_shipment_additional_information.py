# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from mirakl_seller._runtime import ApiModel


class ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation(ApiModel):
    """ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation model."""

    code: StrictStr
    type: StrictStr
    value: StrictStr
