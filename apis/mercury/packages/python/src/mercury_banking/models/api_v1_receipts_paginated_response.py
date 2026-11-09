# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_receipt_response import ApiV1ReceiptResponse
from mercury_banking.models.api_v1_receipts_paginated_response_page import ApiV1ReceiptsPaginatedResponsePage
from mercury_banking._runtime import ApiModel


class ApiV1ReceiptsPaginatedResponse(ApiModel):
    """ApiV1ReceiptsPaginatedResponse model."""

    page: ApiV1ReceiptsPaginatedResponsePage
    receipts: List[ApiV1ReceiptResponse]
