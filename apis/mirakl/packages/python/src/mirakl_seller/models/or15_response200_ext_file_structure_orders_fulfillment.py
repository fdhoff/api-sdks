# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or15_response200_ext_file_structure_orders_fulfillment_center import (
    OR15Response200ExtFileStructureOrdersFulfillmentCenter,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersFulfillment(ApiModel):
    """OR15Response200ExtFileStructureOrdersFulfillment model."""

    center: OR15Response200ExtFileStructureOrdersFulfillmentCenter
