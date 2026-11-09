# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class P31Response200Products(ApiModel):
    """P31Response200Products model."""

    category_code: StrictStr
    category_label: StrictStr
    product_id: StrictStr
    product_id_type: StrictStr
    product_sku: StrictStr
    product_title: StrictStr
