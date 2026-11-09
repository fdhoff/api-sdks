# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.a02_request_address import A02RequestAddress
from mirakl_seller.models.a02_request_payment_info import A02RequestPaymentInfo
from mirakl_seller.models.a02_request_pro_details import A02RequestProDetails
from mirakl_seller.models.a02_request_producer_identifiers import A02RequestProducerIdentifiers
from mirakl_seller.models.a02_request_shop_additional_fields import A02RequestShopAdditionalFields
from mirakl_seller._runtime import ApiModel


class A02Request(ApiModel):
    """A02Request model."""

    address: Optional[A02RequestAddress] = None
    channels: Optional[List[StrictStr]] = None
    closed_from: Optional[datetime] = None
    closed_to: Optional[datetime] = None
    description: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    fax: Optional[StrictStr] = None
    is_professional: Optional[StrictBool] = None
    payment_info: Optional[A02RequestPaymentInfo] = None
    pro_details: Optional[A02RequestProDetails] = None
    producer_identifiers: Optional[
        Annotated[List[A02RequestProducerIdentifiers], Field(min_length=0, max_length=50)]
    ] = None
    recycling_policy: Optional[Annotated[str, Field(strict=True, max_length=5000)]] = None
    return_policy: Optional[StrictStr] = None
    shipping_country: Optional[StrictStr] = None
    shop_additional_fields: Optional[List[A02RequestShopAdditionalFields]] = None
    shop_name: Optional[StrictStr] = None
    web_site: Optional[StrictStr] = None
