# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.s32_request_multipart_form_data_shop_documents_shop_documents import (
    S32RequestMultipartFormDataShopDocumentsShopDocuments,
)
from mirakl_seller._runtime import ApiModel


class S32RequestMultipartFormDataShopDocuments(ApiModel):
    """S32RequestMultipartFormDataShopDocuments model."""

    shop_documents: List[S32RequestMultipartFormDataShopDocumentsShopDocuments]
