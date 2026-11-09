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
    StrictStr,
    model_validator as _model_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, cast as _cast
from mirakl_seller.models.or12_response200_customer import OR12Response200Customer
from mirakl_seller.models.or12_response200_order_lines import OR12Response200OrderLines
from mirakl_seller._runtime import ApiModel


class OR12Response200(ApiModel):
    """OR12Response200 model."""

    acceptance_decision_date: datetime
    commercial_id: StrictStr
    created_date: datetime
    customer: Optional[OR12Response200Customer] = None
    has_customer_message: StrictBool
    has_incident: StrictBool
    has_invoice: StrictBool
    last_updated_date: datetime
    order_id: StrictStr
    order_lines: List[OR12Response200OrderLines]
    order_state: StrictStr
    order_state_reason_code: StrictStr
    order_state_reason_label: StrictStr
    deprecated_payment_type: StrictStr = Field(
        validation_alias=AliasChoices("paymentType", "deprecated_payment_type"), serialization_alias="paymentType"
    )
    payment_type: StrictStr
    price: float
    shipping_company: Optional[StrictStr] = None
    shipping_price: float
    shipping_tracking: Optional[StrictStr] = None
    shipping_tracking_url: Optional[StrictStr] = None
    shipping_type_code: StrictStr
    shipping_type_label: StrictStr
    shipping_zone_code: StrictStr
    shipping_zone_label: StrictStr
    total_commission: float
    total_price: float
