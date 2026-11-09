# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesOrderConditions(ApiModel):
    """PC01Response200FeaturesOrderConditions model."""

    lead_time_to_ship: StrictBool
    maximum_order_quantity: StrictBool
    minimum_order_quantity: StrictBool
    package_order_quantity: StrictBool
