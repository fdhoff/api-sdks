# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer_accounting_contact import (
    OR15Response200ExtFileStructureOrdersCustomerAccountingContact,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer_billing_address import (
    OR15Response200ExtFileStructureOrdersCustomerBillingAddress,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer_delivery_contact import (
    OR15Response200ExtFileStructureOrdersCustomerDeliveryContact,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer_organization import (
    OR15Response200ExtFileStructureOrdersCustomerOrganization,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer_shipping_address import (
    OR15Response200ExtFileStructureOrdersCustomerShippingAddress,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersCustomer(ApiModel):
    """OR15Response200ExtFileStructureOrdersCustomer model."""

    accounting_contact: Optional[OR15Response200ExtFileStructureOrdersCustomerAccountingContact] = None
    billing_address: OR15Response200ExtFileStructureOrdersCustomerBillingAddress
    civility: Optional[StrictStr] = None
    customer_id: StrictStr
    delivery_contact: Optional[OR15Response200ExtFileStructureOrdersCustomerDeliveryContact] = None
    firstname: StrictStr
    lastname: StrictStr
    locale: Optional[StrictStr] = None
    organization: Optional[OR15Response200ExtFileStructureOrdersCustomerOrganization] = None
    shipping_address: OR15Response200ExtFileStructureOrdersCustomerShippingAddress
