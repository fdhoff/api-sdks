# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from mirakl_seller._runtime import ApiModel


class IV01Response200InvoicesAutoInvoicePaymentInfo(ApiModel):
    """IV01Response200InvoicesAutoInvoicePaymentInfo model."""

    type: Optional[StrictStr] = Field(default=None, alias="@type")
    bank_city: Optional[StrictStr] = None
    bank_name: Optional[StrictStr] = None
    bank_street: Optional[StrictStr] = None
    bank_zip: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
