# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.a01_response200_applicable_taxes import A01Response200ApplicableTaxes
from mirakl_seller.models.a01_response200_billing_info import A01Response200BillingInfo
from mirakl_seller.models.a01_response200_contact_informations import A01Response200ContactInformations
from mirakl_seller.models.a01_response200_default_billing_information import A01Response200DefaultBillingInformation
from mirakl_seller.models.a01_response200_dropship import A01Response200Dropship
from mirakl_seller.models.a01_response200_kyc import A01Response200Kyc
from mirakl_seller.models.a01_response200_payment_details import A01Response200PaymentDetails
from mirakl_seller.models.a01_response200_payment_info import A01Response200PaymentInfo
from mirakl_seller.models.a01_response200_pro_details import A01Response200ProDetails
from mirakl_seller.models.a01_response200_producer_identifiers import A01Response200ProducerIdentifiers
from mirakl_seller.models.a01_response200_shipping import A01Response200Shipping
from mirakl_seller.models.a01_response200_shippings import A01Response200Shippings
from mirakl_seller.models.a01_response200_shop_additional_fields import A01Response200ShopAdditionalFields
from mirakl_seller.models.a01_response200_specific_billing_informations import A01Response200SpecificBillingInformations
from mirakl_seller._runtime import ApiModel


class A01Response200(ApiModel):
    """A01Response200 model."""

    applicable_taxes: Optional[List[A01Response200ApplicableTaxes]] = None
    approval_delay: Optional[StrictInt] = None
    approval_rate: Optional[float] = None
    banner: Optional[StrictStr] = None
    billing_info: A01Response200BillingInfo
    channels: List[StrictStr]
    closed_from: Optional[datetime] = None
    closed_to: Optional[datetime] = None
    contact_informations: A01Response200ContactInformations
    currency_iso_code: StrictStr
    date_created: datetime
    default_billing_information: A01Response200DefaultBillingInformation
    description: Optional[StrictStr] = None
    domains: List[StrictStr]
    dropship: Optional[A01Response200Dropship] = None
    evaluations_count: StrictInt
    free_shipping: StrictBool
    grade: Optional[float] = None
    is_professional: StrictBool
    kyc: Optional[A01Response200Kyc] = None
    last_updated_date: datetime
    logo: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    offers_count: StrictInt
    order_messages_response_delay: Optional[StrictInt] = None
    orders_count: StrictInt
    payment_details: A01Response200PaymentDetails
    payment_info: Optional[A01Response200PaymentInfo] = None
    payment_method_mandatory: StrictBool
    premium: StrictBool
    pro_details: A01Response200ProDetails
    producer_identifiers: Optional[List[A01Response200ProducerIdentifiers]] = None
    recycling_policy: Optional[Annotated[str, Field(strict=True, max_length=5000)]] = None
    return_policy: Optional[StrictStr] = None
    shipping: A01Response200Shipping
    shipping_country: Optional[StrictStr] = None
    shipping_types: List[StrictStr]
    shipping_zones: List[StrictStr]
    shippings: Optional[List[A01Response200Shippings]] = None
    shop_additional_fields: List[A01Response200ShopAdditionalFields]
    shop_id: StrictInt
    shop_name: StrictStr
    shop_state: StrictStr
    specific_billing_informations: Optional[List[A01Response200SpecificBillingInformations]] = None
    suspension_type: Optional[StrictStr] = None
