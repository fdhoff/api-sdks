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
from mirakl_seller.models.or15_response200_ext_file_structure_orders_channel import (
    OR15Response200ExtFileStructureOrdersChannel,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer import (
    OR15Response200ExtFileStructureOrdersCustomer,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_delivery_date import (
    OR15Response200ExtFileStructureOrdersDeliveryDate,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_discount_campaigns import (
    OR15Response200ExtFileStructureOrdersDiscountCampaigns,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_fulfillment import (
    OR15Response200ExtFileStructureOrdersFulfillment,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_invoice_details import (
    OR15Response200ExtFileStructureOrdersInvoiceDetails,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_additional_fields import (
    OR15Response200ExtFileStructureOrdersOrderAdditionalFields,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines import (
    OR15Response200ExtFileStructureOrdersOrderLines,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_refunds import (
    OR15Response200ExtFileStructureOrdersOrderRefunds,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_taxes import (
    OR15Response200ExtFileStructureOrdersOrderTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_promotions import (
    OR15Response200ExtFileStructureOrdersPromotions,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_references import (
    OR15Response200ExtFileStructureOrdersReferences,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrders(ApiModel):
    """OR15Response200ExtFileStructureOrders model."""

    acceptance_decision_date: Optional[datetime] = None
    can_cancel: StrictBool
    can_shop_ship: StrictBool
    channel: Optional[OR15Response200ExtFileStructureOrdersChannel] = None
    commercial_id: StrictStr
    created_date: datetime
    currency_iso_code: StrictStr
    customer: OR15Response200ExtFileStructureOrdersCustomer
    customer_debited_date: Optional[datetime] = None
    customer_directly_pays_seller: Optional[StrictBool] = None
    customer_notification_email: Optional[StrictStr] = None
    delivery_date: Optional[OR15Response200ExtFileStructureOrdersDeliveryDate] = None
    discount_campaigns: Optional[List[OR15Response200ExtFileStructureOrdersDiscountCampaigns]] = None
    fulfillment: OR15Response200ExtFileStructureOrdersFulfillment
    fully_refunded: StrictBool
    has_customer_message: StrictBool
    has_incident: StrictBool
    has_invoice: StrictBool
    invoice_details: Optional[OR15Response200ExtFileStructureOrdersInvoiceDetails] = None
    last_updated_date: datetime
    leadtime_to_ship: StrictInt
    order_additional_fields: Optional[List[OR15Response200ExtFileStructureOrdersOrderAdditionalFields]] = None
    order_id: StrictStr
    order_lines: List[OR15Response200ExtFileStructureOrdersOrderLines]
    order_refunds: Optional[List[OR15Response200ExtFileStructureOrdersOrderRefunds]] = None
    order_state: StrictStr
    order_state_reason_code: Optional[StrictStr] = None
    order_state_reason_label: Optional[StrictStr] = None
    order_tax_mode: StrictStr
    order_taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderTaxes]] = None
    deprecated_payment_type: StrictStr = Field(
        validation_alias=AliasChoices("paymentType", "deprecated_payment_type"), serialization_alias="paymentType"
    )
    payment_duration: Optional[StrictInt] = None
    payment_type: Optional[StrictStr] = None
    payment_workflow: Optional[StrictStr] = None
    price: float
    promotions: Optional[OR15Response200ExtFileStructureOrdersPromotions] = None
    quote_id: Optional[StrictStr] = None
    references: Optional[OR15Response200ExtFileStructureOrdersReferences] = None
    shipping_carrier_code: Optional[StrictStr] = None
    shipping_carrier_scac_code: Optional[StrictStr] = None
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
