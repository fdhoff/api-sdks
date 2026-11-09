# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class A01Response200PaymentDetailsSubBalances(ApiModel):
    """A01Response200PaymentDetailsSubBalances model."""

    paid: float
    pay_out_psp_code: StrictStr
    payable: float
    pending: float
