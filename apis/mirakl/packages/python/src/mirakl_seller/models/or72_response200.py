# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or72_response200_order_documents import OR72Response200OrderDocuments
from mirakl_seller._runtime import ApiModel


class OR72Response200(ApiModel):
    """OR72Response200 model."""

    order_documents: List[OR72Response200OrderDocuments]
    total_count: Optional[StrictInt] = None
