# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a02_response200_updated_address import A02Response200UpdatedAddress
from mirakl_seller.models.a02_response200_updated_default_billing_information import (
    A02Response200UpdatedDefaultBillingInformation,
)
from mirakl_seller.models.a02_response200_updated_payment_info import A02Response200UpdatedPaymentInfo
from mirakl_seller.models.a02_response200_updated_pro_details import A02Response200UpdatedProDetails
from mirakl_seller.models.a02_response200_updated_producer_identifiers import A02Response200UpdatedProducerIdentifiers
from mirakl_seller.models.a02_response200_updated_shipping import A02Response200UpdatedShipping
from mirakl_seller.models.a02_response200_updated_shop_additional_fields import (
    A02Response200UpdatedShopAdditionalFields,
)
from mirakl_seller.models.a02_response200_updated_specific_billing_informations import (
    A02Response200UpdatedSpecificBillingInformations,
)
from mirakl_seller._runtime import ApiModel


class A02Response200Updated(ApiModel):
    """A02Response200Updated model."""

    address: Optional[A02Response200UpdatedAddress] = None
    channels: Optional[List[StrictStr]] = None
    closed_from: Optional[datetime] = None
    closed_to: Optional[datetime] = None
    default_billing_information: Optional[A02Response200UpdatedDefaultBillingInformation] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    fax: Optional[StrictStr] = None
    is_professional: Optional[StrictBool] = None
    model: Optional[StrictStr] = None
    payment_info: Optional[A02Response200UpdatedPaymentInfo] = None
    payment_method_mandatory: Optional[StrictBool] = None
    pro_details: Optional[A02Response200UpdatedProDetails] = None
    producer_identifiers: Optional[List[A02Response200UpdatedProducerIdentifiers]] = None
    recycling_policy: Optional[StrictStr] = None
    return_policy: Optional[StrictStr] = None
    shipping: Optional[A02Response200UpdatedShipping] = None
    shipping_country: Optional[StrictStr] = None
    shop_additional_fields: Optional[List[A02Response200UpdatedShopAdditionalFields]] = None
    shop_name: Optional[StrictStr] = None
    specific_billing_informations: Optional[List[A02Response200UpdatedSpecificBillingInformations]] = None
    web_site: Optional[StrictStr] = None
