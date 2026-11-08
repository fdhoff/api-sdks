# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.account_v2.api import (
    combined_shipping_rules_api,
    payout_settings_api,
    rate_tables_api,
    user_preferences_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        combined_shipping_rules_api.OPERATIONS,
        payout_settings_api.OPERATIONS,
        rate_tables_api.OPERATIONS,
        user_preferences_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.combined_shipping_rules = combined_shipping_rules_api.CombinedShippingRulesApi(transport)
        self.payout_settings = payout_settings_api.PayoutSettingsApi(transport)
        self.rate_tables = rate_tables_api.RateTablesApi(transport)
        self.user_preferences = user_preferences_api.UserPreferencesApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.combined_shipping_rules = combined_shipping_rules_api.AsyncCombinedShippingRulesApi(transport)
        self.payout_settings = payout_settings_api.AsyncPayoutSettingsApi(transport)
        self.rate_tables = rate_tables_api.AsyncRateTablesApi(transport)
        self.user_preferences = user_preferences_api.AsyncUserPreferencesApi(transport)
