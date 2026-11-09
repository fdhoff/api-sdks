# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.p31_response200_products import P31Response200Products
from mirakl_seller._runtime import ApiModel


class P31Response200(ApiModel):
    """P31Response200 model."""

    products: List[P31Response200Products]
    total_count: StrictInt
