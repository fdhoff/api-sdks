# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.alert_dimension import AlertDimension
from ebay_sell.marketing.models.aspect import Aspect
from ebay_sell._runtime import ApiModel


class AlertDetails(ApiModel):
    """AlertDetails model."""

    dimension: Optional[AlertDimension] = None
    aspect: Optional[Aspect] = None
