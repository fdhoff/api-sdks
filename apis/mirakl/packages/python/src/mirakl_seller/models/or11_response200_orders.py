# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from collections.abc import Mapping as _Mapping
from datetime import datetime
from pydantic import (
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    ModelWrapValidatorHandler as _ModelWrapValidatorHandler,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator as _model_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, cast as _cast
from mirakl_seller.models.or11_response200_orders_channel import OR11Response200OrdersChannel
from mirakl_seller.models.or11_response200_orders_customer import OR11Response200OrdersCustomer
from mirakl_seller.models.or11_response200_orders_delivery_date import OR11Response200OrdersDeliveryDate
from mirakl_seller.models.or11_response200_orders_discount_campaigns import OR11Response200OrdersDiscountCampaigns
from mirakl_seller.models.or11_response200_orders_fulfillment import OR11Response200OrdersFulfillment
from mirakl_seller.models.or11_response200_orders_invoice_details import OR11Response200OrdersInvoiceDetails
from mirakl_seller.models.or11_response200_orders_order_additional_fields import (
    OR11Response200OrdersOrderAdditionalFields,
)
from mirakl_seller.models.or11_response200_orders_order_lines import OR11Response200OrdersOrderLines
from mirakl_seller.models.or11_response200_orders_order_refunds import OR11Response200OrdersOrderRefunds
from mirakl_seller.models.or11_response200_orders_order_taxes import OR11Response200OrdersOrderTaxes
from mirakl_seller.models.or11_response200_orders_promotions import OR11Response200OrdersPromotions
from mirakl_seller.models.or11_response200_orders_references import OR11Response200OrdersReferences
from mirakl_seller._runtime import ApiModel


class OR11Response200Orders(ApiModel):
    """OR11Response200Orders model."""

    acceptance_decision_date: Optional[datetime] = None
    can_cancel: StrictBool
    can_shop_ship: StrictBool
    channel: Optional[OR11Response200OrdersChannel] = None
    commercial_id: StrictStr
    created_date: datetime
    currency_iso_code: StrictStr
    customer: OR11Response200OrdersCustomer
    customer_debited_date: Optional[datetime] = None
    customer_directly_pays_seller: Optional[StrictBool] = None
    customer_notification_email: Optional[StrictStr] = None
    delivery_date: Optional[OR11Response200OrdersDeliveryDate] = None
    discount_campaigns: Optional[List[OR11Response200OrdersDiscountCampaigns]] = None
    fulfillment: OR11Response200OrdersFulfillment
    fully_refunded: StrictBool
    has_customer_message: StrictBool
    has_incident: StrictBool
    has_invoice: StrictBool
    invoice_details: Optional[OR11Response200OrdersInvoiceDetails] = None
    last_updated_date: datetime
    leadtime_to_ship: StrictInt
    order_additional_fields: Optional[List[OR11Response200OrdersOrderAdditionalFields]] = None
    order_id: StrictStr
    order_lines: List[OR11Response200OrdersOrderLines]
    order_refunds: Optional[List[OR11Response200OrdersOrderRefunds]] = None
    order_state: StrictStr
    order_state_reason_code: Optional[StrictStr] = None
    order_state_reason_label: Optional[StrictStr] = None
    order_tax_mode: StrictStr
    order_taxes: Optional[List[OR11Response200OrdersOrderTaxes]] = None
    deprecated_payment_type: StrictStr = Field(
        validation_alias=AliasChoices("paymentType", "deprecated_payment_type"), serialization_alias="paymentType"
    )
    payment_duration: Optional[StrictInt] = None
    payment_type: Optional[StrictStr] = None
    payment_workflow: Optional[StrictStr] = None
    price: float
    promotions: Optional[OR11Response200OrdersPromotions] = None
    quote_id: Optional[StrictStr] = None
    references: Optional[OR11Response200OrdersReferences] = None
    shipping_carrier_code: Optional[StrictStr] = None
    shipping_carrier_standard_code: Optional[StrictStr] = None
    shipping_company: Optional[StrictStr] = None
    shipping_deadline: Optional[datetime] = None
    shipping_price: float
    shipping_pudo_id: Optional[StrictStr] = None
    shipping_tracking: Optional[StrictStr] = None
    shipping_tracking_url: Optional[StrictStr] = None
    shipping_type_code: StrictStr
    shipping_type_label: StrictStr
    shipping_type_standard_code: Optional[StrictStr] = None
    shipping_zone_code: StrictStr
    shipping_zone_label: StrictStr
    total_commission: float
    total_price: float
    transaction_date: Optional[datetime] = None
    transaction_number: Optional[StrictStr] = None
