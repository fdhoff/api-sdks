# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class ST42Response200DataRatesEstimatedCost(ApiModel):
    """ST42Response200DataRatesEstimatedCost model."""

    amount: float
    currency_iso_code: StrictStr
