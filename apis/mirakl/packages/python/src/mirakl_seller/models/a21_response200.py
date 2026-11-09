# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a21_response200_approval_delay import A21Response200ApprovalDelay
from mirakl_seller.models.a21_response200_approval_rate import A21Response200ApprovalRate
from mirakl_seller.models.a21_response200_auto_refused_rate import A21Response200AutoRefusedRate
from mirakl_seller.models.a21_response200_average_cart import A21Response200AverageCart
from mirakl_seller.models.a21_response200_average_cart_with_shipping import A21Response200AverageCartWithShipping
from mirakl_seller.models.a21_response200_cancelation_rate import A21Response200CancelationRate
from mirakl_seller.models.a21_response200_consecutive_refused_orders_count import (
    A21Response200ConsecutiveRefusedOrdersCount,
)
from mirakl_seller.models.a21_response200_evaluations_count import A21Response200EvaluationsCount
from mirakl_seller.models.a21_response200_grade import A21Response200Grade
from mirakl_seller.models.a21_response200_incident_rate import A21Response200IncidentRate
from mirakl_seller.models.a21_response200_late_shipment_rate import A21Response200LateShipmentRate
from mirakl_seller.models.a21_response200_offers_count import A21Response200OffersCount
from mirakl_seller.models.a21_response200_order_messages_response_delay import A21Response200OrderMessagesResponseDelay
from mirakl_seller.models.a21_response200_orders_count import A21Response200OrdersCount
from mirakl_seller.models.a21_response200_refund_rate import A21Response200RefundRate
from mirakl_seller.models.a21_response200_return_rate import A21Response200ReturnRate
from mirakl_seller.models.a21_response200_shipping_delay import A21Response200ShippingDelay
from mirakl_seller.models.a21_response200_total_revenue import A21Response200TotalRevenue
from mirakl_seller.models.a21_response200_valid_tracking_rate import A21Response200ValidTrackingRate
from mirakl_seller._runtime import ApiModel


class A21Response200(ApiModel):
    """A21Response200 model."""

    approval_delay: Optional[List[A21Response200ApprovalDelay]] = None
    approval_rate: Optional[List[A21Response200ApprovalRate]] = None
    auto_refused_rate: Optional[List[A21Response200AutoRefusedRate]] = None
    average_cart: Optional[List[A21Response200AverageCart]] = None
    average_cart_with_shipping: Optional[List[A21Response200AverageCartWithShipping]] = None
    cancelation_rate: Optional[List[A21Response200CancelationRate]] = None
    channel: Optional[StrictStr] = None
    consecutive_refused_orders_count: Optional[List[A21Response200ConsecutiveRefusedOrdersCount]] = None
    evaluations_count: Optional[List[A21Response200EvaluationsCount]] = None
    grade: Optional[List[A21Response200Grade]] = None
    incident_rate: Optional[List[A21Response200IncidentRate]] = None
    last_updated_date: Optional[datetime] = None
    late_shipment_rate: Optional[List[A21Response200LateShipmentRate]] = None
    offers_count: Optional[List[A21Response200OffersCount]] = None
    order_messages_response_delay: Optional[List[A21Response200OrderMessagesResponseDelay]] = None
    orders_count: Optional[List[A21Response200OrdersCount]] = None
    refund_rate: Optional[List[A21Response200RefundRate]] = None
    return_rate: Optional[List[A21Response200ReturnRate]] = None
    shipping_delay: Optional[List[A21Response200ShippingDelay]] = None
    shop_id: Optional[StrictInt] = None
    total_revenue: Optional[List[A21Response200TotalRevenue]] = None
    valid_tracking_rate: Optional[List[A21Response200ValidTrackingRate]] = None
