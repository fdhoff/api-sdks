# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller.models.buyback_kyc_documents import BuybackKycDocuments
from backmarket_seller._runtime import ApiModel


class BuybackOrderCustomerDocumentsInner(ApiModel):
    """BuybackOrderCustomerDocumentsInner model."""

    type: BuybackKycDocuments
    url: StrictStr
