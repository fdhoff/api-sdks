# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.s30_response200_shop_documents import S30Response200ShopDocuments
from mirakl_seller._runtime import ApiModel


class S30Response200(ApiModel):
    """S30Response200 model."""

    shop_documents: List[S30Response200ShopDocuments]
    total_count: Optional[StrictInt] = None
