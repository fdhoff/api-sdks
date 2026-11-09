# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl05_response200_ext_file_structure_entities import TL05Response200ExtFileStructureEntities
from mirakl_seller._runtime import ApiModel


class TL05Response200ExtFileStructure(ApiModel):
    """TL05Response200ExtFileStructure model."""

    accounting_document_creation_date: Optional[datetime] = None
    accounting_document_id: Optional[StrictStr] = None
    accounting_document_number: Optional[StrictStr] = None
    amount: Optional[float] = None
    amount_credited: Optional[float] = None
    amount_debited: Optional[float] = None
    balance: Optional[float] = None
    currency_iso_code: Optional[StrictStr] = None
    date_created: Optional[datetime] = None
    entities: Optional[TL05Response200ExtFileStructureEntities] = None
    id: Optional[StrictStr] = None
    last_updated: Optional[datetime] = None
    pay_out_psp_code: Optional[StrictStr] = None
    payment_state: Optional[StrictStr] = None
    psp_balance: Optional[float] = None
    seller_billing_cycle_id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
