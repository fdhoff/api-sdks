# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr75_response200_requests_errors import DR75Response200RequestsErrors
from mirakl_seller.models.dr75_response200_requests_input import DR75Response200RequestsInput
from mirakl_seller._runtime import ApiModel


class DR75Response200Requests(ApiModel):
    """DR75Response200Requests model."""

    errors: Optional[List[DR75Response200RequestsErrors]] = None
    input: DR75Response200RequestsInput
