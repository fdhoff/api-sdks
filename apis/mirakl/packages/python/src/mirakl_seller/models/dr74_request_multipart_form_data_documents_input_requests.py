# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr74_request_multipart_form_data_documents_input_requests_files import (
    DR74RequestMultipartFormDataDocumentsInputRequestsFiles,
)
from mirakl_seller._runtime import ApiModel


class DR74RequestMultipartFormDataDocumentsInputRequests(ApiModel):
    """DR74RequestMultipartFormDataDocumentsInputRequests model."""

    document_number: StrictStr
    due_date: Optional[datetime] = None
    files: List[DR74RequestMultipartFormDataDocumentsInputRequestsFiles]
    issue_date: Optional[datetime] = None
    request_id: StrictStr
    total_amount_excluding_taxes: Optional[float] = None
    total_tax_amount: Optional[float] = None
