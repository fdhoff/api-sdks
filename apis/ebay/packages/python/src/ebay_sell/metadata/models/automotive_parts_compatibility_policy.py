# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class AutomotivePartsCompatibilityPolicy(ApiModel):
    """AutomotivePartsCompatibilityPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    compatibility_based_on: Optional[StrictStr] = Field(default=None, alias="compatibilityBasedOn")
    compatible_vehicle_types: Optional[List[StrictStr]] = Field(default=None, alias="compatibleVehicleTypes")
    max_number_of_compatible_vehicles: Optional[StrictInt] = Field(default=None, alias="maxNumberOfCompatibleVehicles")
