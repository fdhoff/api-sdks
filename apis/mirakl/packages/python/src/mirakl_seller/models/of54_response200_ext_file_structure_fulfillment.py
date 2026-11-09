# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of54_response200_ext_file_structure_fulfillment_center import (
    OF54Response200ExtFileStructureFulfillmentCenter,
)
from mirakl_seller._runtime import ApiModel


class OF54Response200ExtFileStructureFulfillment(ApiModel):
    """OF54Response200ExtFileStructureFulfillment model."""

    center: Optional[OF54Response200ExtFileStructureFulfillmentCenter] = None
