# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or74_response200_order_documents_errors import OR74Response200OrderDocumentsErrors
from mirakl_seller.models.or74_response200_order_documents_input import OR74Response200OrderDocumentsInput
from mirakl_seller._runtime import ApiModel


class OR74Response200OrderDocuments(ApiModel):
    """OR74Response200OrderDocuments model."""

    errors: List[OR74Response200OrderDocumentsErrors]
    input: Optional[OR74Response200OrderDocumentsInput] = None
