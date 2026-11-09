# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.s32_response200_documents import S32Response200Documents
from mirakl_seller._runtime import ApiModel


class S32Response200(ApiModel):
    """S32Response200 model."""

    documents: List[S32Response200Documents]
    errors_count: Optional[StrictInt] = None
