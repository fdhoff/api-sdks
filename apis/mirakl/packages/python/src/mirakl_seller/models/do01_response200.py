# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.do01_response200_documents import DO01Response200Documents
from mirakl_seller._runtime import ApiModel


class DO01Response200(ApiModel):
    """DO01Response200 model."""

    documents: List[DO01Response200Documents]
