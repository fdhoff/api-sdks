# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.create_receipt_shipment_request_customs_data_inner import (
    CreateReceiptShipmentRequestCustomsDataInner,
)
from etsy_seller._runtime import ApiModel


class CreateReceiptShipmentRequest(ApiModel):
    """CreateReceiptShipmentRequest model."""

    tracking_code: Optional[StrictStr] = None
    carrier_name: Optional[StrictStr] = None
    send_bcc: Optional[StrictBool] = None
    note_to_buyer: Optional[StrictStr] = None
    mail_class: Optional[StrictStr] = None
    weight: Optional[float] = None
    weight_units: Optional[StrictStr] = None
    length: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    dimension_units: Optional[StrictStr] = None
    shipping_label_cost: Optional[float] = None
    shipping_label_currency: Optional[StrictStr] = None
    revenue_eligibility: Optional[StrictStr] = None
    ship_from_country: Optional[StrictStr] = None
    ship_to_country: Optional[StrictStr] = None
    incoterm: Optional[StrictStr] = None
    customs_data: Optional[List[CreateReceiptShipmentRequestCustomsDataInner]] = None
    duty_amount: Optional[float] = None
    duty_currency: Optional[StrictStr] = None
    ship_date: Optional[StrictStr] = None
