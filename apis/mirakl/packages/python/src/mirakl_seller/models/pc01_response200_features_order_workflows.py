# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesOrderWorkflows(ApiModel):
    """PC01Response200FeaturesOrderWorkflows model."""

    no_customer_payment_confirmation: StrictBool
    order_acceptance: StrictStr
    pause_debit_workflow: StrictBool
    pay_on_due_date: StrictBool
    pay_on_shipment: StrictBool
    sellers_edit_shipping_origin: StrictBool
    shipping_and_billing_details_before_acceptance: StrictBool
