# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_entities_delivery_bill_information import (
    DR11Response200DataEntitiesDeliveryBillInformation,
)
from mirakl_seller.models.dr11_response200_data_entities_order_additional_fields import (
    DR11Response200DataEntitiesOrderAdditionalFields,
)
from mirakl_seller.models.dr11_response200_data_entities_shipping_information import (
    DR11Response200DataEntitiesShippingInformation,
)
from mirakl_seller.models.dr11_response200_data_entities_shop_billing_cycle import (
    DR11Response200DataEntitiesShopBillingCycle,
)
from mirakl_seller._runtime import ApiModel


class DR11Response200DataEntities(ApiModel):
    """DR11Response200DataEntities model."""

    delivery_bill_information: Optional[List[DR11Response200DataEntitiesDeliveryBillInformation]] = None
    order_additional_fields: Optional[List[DR11Response200DataEntitiesOrderAdditionalFields]] = None
    ship_to_iso_country_code: Optional[StrictStr] = None
    shipping_information: Optional[DR11Response200DataEntitiesShippingInformation] = None
    shop_billing_cycle: Optional[DR11Response200DataEntitiesShopBillingCycle] = None
