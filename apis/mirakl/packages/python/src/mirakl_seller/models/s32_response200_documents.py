# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.s32_response200_documents_errors import S32Response200DocumentsErrors
from mirakl_seller._runtime import ApiModel


class S32Response200Documents(ApiModel):
    """S32Response200Documents model."""

    errors: List[S32Response200DocumentsErrors]
