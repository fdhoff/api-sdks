# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.payment_dispute_activity import PaymentDisputeActivity
from ebay_sell._runtime import ApiModel


class PaymentDisputeActivityHistory(ApiModel):
    """PaymentDisputeActivityHistory model."""

    activity: Optional[List[PaymentDisputeActivity]] = None
