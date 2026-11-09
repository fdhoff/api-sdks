# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class TL03Request(ApiModel):
    """TL03Request model."""

    accounting_document_id: Optional[StrictStr] = None
    accounting_document_number: Optional[StrictStr] = None
    date_created_from: Optional[datetime] = None
    date_created_to: Optional[datetime] = None
    format: Optional[StrictStr] = None
    items_per_chunk: Optional[StrictInt] = None
    last_updated_from: Optional[datetime] = None
    megabytes_per_chunk: Optional[StrictInt] = None
    order_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    order_line_id: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    order_reference_for_customer: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    order_reference_for_seller: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    other_reference: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    pay_out_psp_codes: Optional[List[StrictStr]] = None
    payment_state: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    payment_voucher_number: Optional[StrictStr] = None
    seller_billing_cycle_id: Optional[
        Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=0, max_length=100)]
    ] = None
    shop_domain: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
    shop_id: Optional[StrictInt] = None
    shop_model: Optional[List[StrictStr]] = None
    transaction_date_from: Optional[datetime] = None
    transaction_date_to: Optional[datetime] = None
    transaction_type: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=100)]] = None
