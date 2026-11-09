# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st23_request_shipments_tracking import ST23RequestShipmentsTracking
from mirakl_seller._runtime import ApiModel


class ST23RequestShipments(ApiModel):
    """ST23RequestShipments model."""

    id: StrictStr
    tracking: ST23RequestShipmentsTracking
