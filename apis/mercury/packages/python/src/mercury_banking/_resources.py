# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from mercury_banking._runtime import AsyncTransport, Operation, SyncTransport
from mercury_banking.api import (
    accounts_api,
    auto_transfer_rules_api,
    budgets_api,
    cards_api,
    categories_api,
    credit_api,
    customers_api,
    events_api,
    invoices_api,
    merchants_api,
    organization_api,
    receipts_api,
    recipient_invites_api,
    recipients_api,
    safes_api,
    send_money_requests_api,
    statements_api,
    transactions_api,
    transfer_requests_api,
    treasury_api,
    users_api,
    webhooks_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        accounts_api.OPERATIONS,
        auto_transfer_rules_api.OPERATIONS,
        budgets_api.OPERATIONS,
        cards_api.OPERATIONS,
        categories_api.OPERATIONS,
        credit_api.OPERATIONS,
        customers_api.OPERATIONS,
        events_api.OPERATIONS,
        invoices_api.OPERATIONS,
        merchants_api.OPERATIONS,
        organization_api.OPERATIONS,
        receipts_api.OPERATIONS,
        recipient_invites_api.OPERATIONS,
        recipients_api.OPERATIONS,
        safes_api.OPERATIONS,
        send_money_requests_api.OPERATIONS,
        statements_api.OPERATIONS,
        transactions_api.OPERATIONS,
        transfer_requests_api.OPERATIONS,
        treasury_api.OPERATIONS,
        users_api.OPERATIONS,
        webhooks_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.accounts = accounts_api.AccountsApi(transport)
        self.auto_transfer_rules = auto_transfer_rules_api.AutoTransferRulesApi(transport)
        self.budgets = budgets_api.BudgetsApi(transport)
        self.cards = cards_api.CardsApi(transport)
        self.categories = categories_api.CategoriesApi(transport)
        self.credit = credit_api.CreditApi(transport)
        self.customers = customers_api.CustomersApi(transport)
        self.events = events_api.EventsApi(transport)
        self.invoices = invoices_api.InvoicesApi(transport)
        self.merchants = merchants_api.MerchantsApi(transport)
        self.organization = organization_api.OrganizationApi(transport)
        self.receipts = receipts_api.ReceiptsApi(transport)
        self.recipient_invites = recipient_invites_api.RecipientInvitesApi(transport)
        self.recipients = recipients_api.RecipientsApi(transport)
        self.safes = safes_api.SafesApi(transport)
        self.send_money_requests = send_money_requests_api.SendMoneyRequestsApi(transport)
        self.statements = statements_api.StatementsApi(transport)
        self.transactions = transactions_api.TransactionsApi(transport)
        self.transfer_requests = transfer_requests_api.TransferRequestsApi(transport)
        self.treasury = treasury_api.TreasuryApi(transport)
        self.users = users_api.UsersApi(transport)
        self.webhooks = webhooks_api.WebhooksApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.accounts = accounts_api.AsyncAccountsApi(transport)
        self.auto_transfer_rules = auto_transfer_rules_api.AsyncAutoTransferRulesApi(transport)
        self.budgets = budgets_api.AsyncBudgetsApi(transport)
        self.cards = cards_api.AsyncCardsApi(transport)
        self.categories = categories_api.AsyncCategoriesApi(transport)
        self.credit = credit_api.AsyncCreditApi(transport)
        self.customers = customers_api.AsyncCustomersApi(transport)
        self.events = events_api.AsyncEventsApi(transport)
        self.invoices = invoices_api.AsyncInvoicesApi(transport)
        self.merchants = merchants_api.AsyncMerchantsApi(transport)
        self.organization = organization_api.AsyncOrganizationApi(transport)
        self.receipts = receipts_api.AsyncReceiptsApi(transport)
        self.recipient_invites = recipient_invites_api.AsyncRecipientInvitesApi(transport)
        self.recipients = recipients_api.AsyncRecipientsApi(transport)
        self.safes = safes_api.AsyncSafesApi(transport)
        self.send_money_requests = send_money_requests_api.AsyncSendMoneyRequestsApi(transport)
        self.statements = statements_api.AsyncStatementsApi(transport)
        self.transactions = transactions_api.AsyncTransactionsApi(transport)
        self.transfer_requests = transfer_requests_api.AsyncTransferRequestsApi(transport)
        self.treasury = treasury_api.AsyncTreasuryApi(transport)
        self.users = users_api.AsyncUsersApi(transport)
        self.webhooks = webhooks_api.AsyncWebhooksApi(transport)
