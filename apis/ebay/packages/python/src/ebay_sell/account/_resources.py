# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.account.api import (
    advertising_eligibility_api,
    custom_policies_api,
    fulfillment_policies_api,
    kyc_api,
    payment_policies_api,
    payments_programs_api,
    privileges_api,
    programs_api,
    rate_tables_api,
    return_policies_api,
    sales_taxes_api,
    subscriptions_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        advertising_eligibility_api.OPERATIONS,
        custom_policies_api.OPERATIONS,
        fulfillment_policies_api.OPERATIONS,
        kyc_api.OPERATIONS,
        payment_policies_api.OPERATIONS,
        payments_programs_api.OPERATIONS,
        privileges_api.OPERATIONS,
        programs_api.OPERATIONS,
        rate_tables_api.OPERATIONS,
        return_policies_api.OPERATIONS,
        sales_taxes_api.OPERATIONS,
        subscriptions_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.advertising_eligibility = advertising_eligibility_api.AdvertisingEligibilityApi(transport)
        self.custom_policies = custom_policies_api.CustomPoliciesApi(transport)
        self.fulfillment_policies = fulfillment_policies_api.FulfillmentPoliciesApi(transport)
        self.kyc = kyc_api.KycApi(transport)
        self.payment_policies = payment_policies_api.PaymentPoliciesApi(transport)
        self.payments_programs = payments_programs_api.PaymentsProgramsApi(transport)
        self.privileges = privileges_api.PrivilegesApi(transport)
        self.programs = programs_api.ProgramsApi(transport)
        self.rate_tables = rate_tables_api.RateTablesApi(transport)
        self.return_policies = return_policies_api.ReturnPoliciesApi(transport)
        self.sales_taxes = sales_taxes_api.SalesTaxesApi(transport)
        self.subscriptions = subscriptions_api.SubscriptionsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.advertising_eligibility = advertising_eligibility_api.AsyncAdvertisingEligibilityApi(transport)
        self.custom_policies = custom_policies_api.AsyncCustomPoliciesApi(transport)
        self.fulfillment_policies = fulfillment_policies_api.AsyncFulfillmentPoliciesApi(transport)
        self.kyc = kyc_api.AsyncKycApi(transport)
        self.payment_policies = payment_policies_api.AsyncPaymentPoliciesApi(transport)
        self.payments_programs = payments_programs_api.AsyncPaymentsProgramsApi(transport)
        self.privileges = privileges_api.AsyncPrivilegesApi(transport)
        self.programs = programs_api.AsyncProgramsApi(transport)
        self.rate_tables = rate_tables_api.AsyncRateTablesApi(transport)
        self.return_policies = return_policies_api.AsyncReturnPoliciesApi(transport)
        self.sales_taxes = sales_taxes_api.AsyncSalesTaxesApi(transport)
        self.subscriptions = subscriptions_api.AsyncSubscriptionsApi(transport)
