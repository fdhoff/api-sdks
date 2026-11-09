# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_recipient_billing_address import (
    DR11Response200DataRecipientBillingAddress,
)
from mirakl_seller.models.dr11_response200_data_recipient_organization import DR11Response200DataRecipientOrganization
from mirakl_seller.models.dr11_response200_data_recipient_shipping_address import (
    DR11Response200DataRecipientShippingAddress,
)
from mirakl_seller._runtime import ApiModel


class DR11Response200DataRecipient(ApiModel):
    """DR11Response200DataRecipient model."""

    billing_address: DR11Response200DataRecipientBillingAddress
    id: StrictStr
    locale: Optional[StrictStr] = None
    organization: Optional[DR11Response200DataRecipientOrganization] = None
    shipping_address: Optional[DR11Response200DataRecipientShippingAddress] = None
    type: Optional[StrictStr] = None
