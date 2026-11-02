# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.buyback_order_customer_documents_inner import BuybackOrderCustomerDocumentsInner
from backmarket_seller._runtime import ApiModel


class BuybackOrderCustomer(ApiModel):
    """BuybackOrderCustomer model."""

    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    phone: Optional[StrictStr] = None
    date_of_birth: Optional[StrictStr] = Field(default=None, alias="dateOfBirth")
    documents: Optional[List[BuybackOrderCustomerDocumentsInner]] = None
