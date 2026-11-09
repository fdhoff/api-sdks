# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr12_response200_data_product_references import DR12Response200DataProductReferences
from mirakl_seller._runtime import ApiModel


class DR12Response200DataProduct(ApiModel):
    """DR12Response200DataProduct model."""

    references: List[DR12Response200DataProductReferences]
    sku: Optional[StrictStr] = None
    title: StrictStr
