# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p11_response200_products import P11Response200Products
from mirakl_seller._runtime import ApiModel


class P11Response200(ApiModel):
    """P11Response200 model."""

    products: Optional[List[P11Response200Products]] = None
