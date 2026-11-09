# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.sh52_response200_configuration_prices import SH52Response200ConfigurationPrices
from mirakl_seller._runtime import ApiModel


class SH52Response200Configuration(ApiModel):
    """SH52Response200Configuration model."""

    logistic_class_code: StrictStr
    overridden_by_shop: StrictBool
    prices: SH52Response200ConfigurationPrices
    shipping_method_code: StrictStr
    shipping_zone_code: StrictStr
