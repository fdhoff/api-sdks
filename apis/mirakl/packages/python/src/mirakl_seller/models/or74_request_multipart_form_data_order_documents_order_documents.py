# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or74_request_multipart_form_data_order_documents_order_documents_entity import (
    OR74RequestMultipartFormDataOrderDocumentsOrderDocumentsEntity,
)
from mirakl_seller._runtime import ApiModel


class OR74RequestMultipartFormDataOrderDocumentsOrderDocuments(ApiModel):
    """OR74RequestMultipartFormDataOrderDocumentsOrderDocuments model."""

    entity: Optional[OR74RequestMultipartFormDataOrderDocumentsOrderDocumentsEntity] = None
    file_name: StrictStr
    type_code: StrictStr
