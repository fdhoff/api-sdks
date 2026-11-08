# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.product_safety_label_pictogram import ProductSafetyLabelPictogram
from ebay_sell.metadata.models.product_safety_label_statement import ProductSafetyLabelStatement
from ebay_sell._runtime import ApiModel


class ProductSafetyLabelsResponse(ApiModel):
    """ProductSafetyLabelsResponse model."""

    pictograms: Optional[List[ProductSafetyLabelPictogram]] = None
    statements: Optional[List[ProductSafetyLabelStatement]] = None
