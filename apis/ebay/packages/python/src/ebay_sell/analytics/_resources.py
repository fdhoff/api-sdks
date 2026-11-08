# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.analytics.api import customer_service_metrics_api, seller_standards_profiles_api, traffic_reports_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        customer_service_metrics_api.OPERATIONS,
        seller_standards_profiles_api.OPERATIONS,
        traffic_reports_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.customer_service_metrics = customer_service_metrics_api.CustomerServiceMetricsApi(transport)
        self.seller_standards_profiles = seller_standards_profiles_api.SellerStandardsProfilesApi(transport)
        self.traffic_reports = traffic_reports_api.TrafficReportsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.customer_service_metrics = customer_service_metrics_api.AsyncCustomerServiceMetricsApi(transport)
        self.seller_standards_profiles = seller_standards_profiles_api.AsyncSellerStandardsProfilesApi(transport)
        self.traffic_reports = traffic_reports_api.AsyncTrafficReportsApi(transport)
