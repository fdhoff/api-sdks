# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or12_response200_customer_billing_address import OR12Response200CustomerBillingAddress
from mirakl_seller.models.or12_response200_customer_shipping_address import OR12Response200CustomerShippingAddress
from mirakl_seller._runtime import ApiModel


class OR12Response200Customer(ApiModel):
    """OR12Response200Customer model."""

    billing_address: OR12Response200CustomerBillingAddress
    civility: Optional[StrictStr] = None
    customer_id: StrictStr
    firstname: StrictStr
    lastname: StrictStr
    shipping_address: OR12Response200CustomerShippingAddress
