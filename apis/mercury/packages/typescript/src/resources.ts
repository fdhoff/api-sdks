// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { AccountsApi, OPERATIONS as AccountsApiOperations } from './apis/AccountsApi.js';
import { AutoTransferRulesApi, OPERATIONS as AutoTransferRulesApiOperations } from './apis/AutoTransferRulesApi.js';
import { BudgetsApi, OPERATIONS as BudgetsApiOperations } from './apis/BudgetsApi.js';
import { CardsApi, OPERATIONS as CardsApiOperations } from './apis/CardsApi.js';
import { CategoriesApi, OPERATIONS as CategoriesApiOperations } from './apis/CategoriesApi.js';
import { CreditApi, OPERATIONS as CreditApiOperations } from './apis/CreditApi.js';
import { CustomersApi, OPERATIONS as CustomersApiOperations } from './apis/CustomersApi.js';
import { EventsApi, OPERATIONS as EventsApiOperations } from './apis/EventsApi.js';
import { InvoicesApi, OPERATIONS as InvoicesApiOperations } from './apis/InvoicesApi.js';
import { MerchantsApi, OPERATIONS as MerchantsApiOperations } from './apis/MerchantsApi.js';
import { OrganizationApi, OPERATIONS as OrganizationApiOperations } from './apis/OrganizationApi.js';
import { ProductsApi, OPERATIONS as ProductsApiOperations } from './apis/ProductsApi.js';
import { ReceiptsApi, OPERATIONS as ReceiptsApiOperations } from './apis/ReceiptsApi.js';
import { RecipientInvitesApi, OPERATIONS as RecipientInvitesApiOperations } from './apis/RecipientInvitesApi.js';
import { RecipientsApi, OPERATIONS as RecipientsApiOperations } from './apis/RecipientsApi.js';
import { SafesApi, OPERATIONS as SafesApiOperations } from './apis/SafesApi.js';
import { SendMoneyRequestsApi, OPERATIONS as SendMoneyRequestsApiOperations } from './apis/SendMoneyRequestsApi.js';
import { StatementsApi, OPERATIONS as StatementsApiOperations } from './apis/StatementsApi.js';
import { TransactionsApi, OPERATIONS as TransactionsApiOperations } from './apis/TransactionsApi.js';
import { TransferRequestsApi, OPERATIONS as TransferRequestsApiOperations } from './apis/TransferRequestsApi.js';
import { TreasuryApi, OPERATIONS as TreasuryApiOperations } from './apis/TreasuryApi.js';
import { UsersApi, OPERATIONS as UsersApiOperations } from './apis/UsersApi.js';
import { WebhooksApi, OPERATIONS as WebhooksApiOperations } from './apis/WebhooksApi.js';
import type { Operation, Transport } from './runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...AccountsApiOperations,
    ...AutoTransferRulesApiOperations,
    ...BudgetsApiOperations,
    ...CardsApiOperations,
    ...CategoriesApiOperations,
    ...CreditApiOperations,
    ...CustomersApiOperations,
    ...EventsApiOperations,
    ...InvoicesApiOperations,
    ...MerchantsApiOperations,
    ...OrganizationApiOperations,
    ...ProductsApiOperations,
    ...ReceiptsApiOperations,
    ...RecipientInvitesApiOperations,
    ...RecipientsApiOperations,
    ...SafesApiOperations,
    ...SendMoneyRequestsApiOperations,
    ...StatementsApiOperations,
    ...TransactionsApiOperations,
    ...TransferRequestsApiOperations,
    ...TreasuryApiOperations,
    ...UsersApiOperations,
    ...WebhooksApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly accounts: AccountsApi;
  readonly autoTransferRules: AutoTransferRulesApi;
  readonly budgets: BudgetsApi;
  readonly cards: CardsApi;
  readonly categories: CategoriesApi;
  readonly credit: CreditApi;
  readonly customers: CustomersApi;
  readonly events: EventsApi;
  readonly invoices: InvoicesApi;
  readonly merchants: MerchantsApi;
  readonly organization: OrganizationApi;
  readonly products: ProductsApi;
  readonly receipts: ReceiptsApi;
  readonly recipientInvites: RecipientInvitesApi;
  readonly recipients: RecipientsApi;
  readonly safes: SafesApi;
  readonly sendMoneyRequests: SendMoneyRequestsApi;
  readonly statements: StatementsApi;
  readonly transactions: TransactionsApi;
  readonly transferRequests: TransferRequestsApi;
  readonly treasury: TreasuryApi;
  readonly users: UsersApi;
  readonly webhooks: WebhooksApi;

  constructor(transport: Transport) {
    this.accounts = new AccountsApi(transport);
    this.autoTransferRules = new AutoTransferRulesApi(transport);
    this.budgets = new BudgetsApi(transport);
    this.cards = new CardsApi(transport);
    this.categories = new CategoriesApi(transport);
    this.credit = new CreditApi(transport);
    this.customers = new CustomersApi(transport);
    this.events = new EventsApi(transport);
    this.invoices = new InvoicesApi(transport);
    this.merchants = new MerchantsApi(transport);
    this.organization = new OrganizationApi(transport);
    this.products = new ProductsApi(transport);
    this.receipts = new ReceiptsApi(transport);
    this.recipientInvites = new RecipientInvitesApi(transport);
    this.recipients = new RecipientsApi(transport);
    this.safes = new SafesApi(transport);
    this.sendMoneyRequests = new SendMoneyRequestsApi(transport);
    this.statements = new StatementsApi(transport);
    this.transactions = new TransactionsApi(transport);
    this.transferRequests = new TransferRequestsApi(transport);
    this.treasury = new TreasuryApi(transport);
    this.users = new UsersApi(transport);
    this.webhooks = new WebhooksApi(transport);
  }
}
