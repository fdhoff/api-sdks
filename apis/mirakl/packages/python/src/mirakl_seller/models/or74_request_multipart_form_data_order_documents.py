# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or74_request_multipart_form_data_order_documents_order_documents import (
    OR74RequestMultipartFormDataOrderDocumentsOrderDocuments,
)
from mirakl_seller._runtime import ApiModel


class OR74RequestMultipartFormDataOrderDocuments(ApiModel):
    """OR74RequestMultipartFormDataOrderDocuments model."""

    order_documents: List[OR74RequestMultipartFormDataOrderDocumentsOrderDocuments]
