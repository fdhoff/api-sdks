# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_customer_accounting_contact import (
    OR11Response200OrdersCustomerAccountingContact,
)
from mirakl_seller.models.or11_response200_orders_customer_billing_address import (
    OR11Response200OrdersCustomerBillingAddress,
)
from mirakl_seller.models.or11_response200_orders_customer_delivery_contact import (
    OR11Response200OrdersCustomerDeliveryContact,
)
from mirakl_seller.models.or11_response200_orders_customer_organization import OR11Response200OrdersCustomerOrganization
from mirakl_seller.models.or11_response200_orders_customer_shipping_address import (
    OR11Response200OrdersCustomerShippingAddress,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersCustomer(ApiModel):
    """OR11Response200OrdersCustomer model."""

    accounting_contact: Optional[OR11Response200OrdersCustomerAccountingContact] = None
    billing_address: OR11Response200OrdersCustomerBillingAddress
    civility: Optional[StrictStr] = None
    customer_id: StrictStr
    delivery_contact: Optional[OR11Response200OrdersCustomerDeliveryContact] = None
    firstname: StrictStr
    lastname: StrictStr
    locale: Optional[StrictStr] = None
    organization: Optional[OR11Response200OrdersCustomerOrganization] = None
    shipping_address: OR11Response200OrdersCustomerShippingAddress
