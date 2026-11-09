# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or74_response200_order_documents import OR74Response200OrderDocuments
from mirakl_seller._runtime import ApiModel


class OR74Response200(ApiModel):
    """OR74Response200 model."""

    errors_count: Optional[StrictInt] = None
    order_documents: List[OR74Response200OrderDocuments]
