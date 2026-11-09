# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.sbc11_response200_data_pay_out import SBC11Response200DataPayOut
from mirakl_seller.models.sbc11_response200_data_shop import SBC11Response200DataShop
from mirakl_seller.models.sbc11_response200_data_summary import SBC11Response200DataSummary
from mirakl_seller._runtime import ApiModel


class SBC11Response200Data(ApiModel):
    """SBC11Response200Data model."""

    amount_transferred_to_operator: Optional[float] = None
    amount_transferred_to_seller: Optional[float] = None
    currency_iso_code: Optional[StrictStr] = None
    date_created: Optional[datetime] = None
    id: Optional[StrictStr] = None
    pay_out: Optional[SBC11Response200DataPayOut] = None
    pay_out_psp_code: Optional[StrictStr] = None
    payment_voucher_number: Optional[StrictStr] = None
    shop: Optional[SBC11Response200DataShop] = None
    summary: Optional[SBC11Response200DataSummary] = None
