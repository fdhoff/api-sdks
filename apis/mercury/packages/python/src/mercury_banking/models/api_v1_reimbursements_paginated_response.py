# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_reimbursement_list_item import ApiV1ReimbursementListItem
from mercury_banking.models.api_v1_reimbursements_paginated_response_page import (
    ApiV1ReimbursementsPaginatedResponsePage,
)
from mercury_banking._runtime import ApiModel


class ApiV1ReimbursementsPaginatedResponse(ApiModel):
    """ApiV1ReimbursementsPaginatedResponse model."""

    page: ApiV1ReimbursementsPaginatedResponsePage
    reimbursements: List[ApiV1ReimbursementListItem]
