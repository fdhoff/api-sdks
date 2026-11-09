# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_ar_invoices_data import ApiV1ArInvoicesData
from mercury_banking.models.api_v1_ar_invoices_paginated_response_page import ApiV1ArInvoicesPaginatedResponsePage
from mercury_banking._runtime import ApiModel


class ApiV1ArInvoicesPaginatedResponse(ApiModel):
    """ApiV1ArInvoicesPaginatedResponse model."""

    invoices: List[ApiV1ArInvoicesData]
    page: ApiV1ArInvoicesPaginatedResponsePage
