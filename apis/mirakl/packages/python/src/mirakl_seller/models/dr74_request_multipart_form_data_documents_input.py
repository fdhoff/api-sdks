# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.dr74_request_multipart_form_data_documents_input_requests import (
    DR74RequestMultipartFormDataDocumentsInputRequests,
)
from mirakl_seller._runtime import ApiModel


class DR74RequestMultipartFormDataDocumentsInput(ApiModel):
    """DR74RequestMultipartFormDataDocumentsInput model."""

    requests: List[DR74RequestMultipartFormDataDocumentsInputRequests]
