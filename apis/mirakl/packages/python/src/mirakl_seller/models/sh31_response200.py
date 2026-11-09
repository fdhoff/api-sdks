# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.sh31_response200_logistic_classes import SH31Response200LogisticClasses
from mirakl_seller._runtime import ApiModel


class SH31Response200(ApiModel):
    """SH31Response200 model."""

    logistic_classes: List[SH31Response200LogisticClasses]
