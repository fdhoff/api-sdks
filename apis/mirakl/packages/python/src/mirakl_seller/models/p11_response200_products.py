# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p11_response200_products_measurement import P11Response200ProductsMeasurement
from mirakl_seller.models.p11_response200_products_offers import P11Response200ProductsOffers
from mirakl_seller.models.p11_response200_products_product_media import P11Response200ProductsProductMedia
from mirakl_seller.models.p11_response200_products_product_references import P11Response200ProductsProductReferences
from mirakl_seller._runtime import ApiModel


class P11Response200Products(ApiModel):
    """P11Response200Products model."""

    category_code: StrictStr
    category_label: StrictStr
    measurement: Optional[P11Response200ProductsMeasurement] = None
    offers: Optional[List[P11Response200ProductsOffers]] = None
    product_brand: Optional[StrictStr] = None
    product_description: Optional[StrictStr] = None
    product_media: Optional[P11Response200ProductsProductMedia] = None
    product_references: List[P11Response200ProductsProductReferences]
    product_sku: StrictStr
    product_title: StrictStr
    total_count: StrictInt
