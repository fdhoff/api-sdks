# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* `client.Products.DeleteAsync`, to delete an invoicing product.

## 0.1.0-alpha.2 (2026-11-10)

* `client.Products.ListAsync`, `client.Products.ListAllAsync` and `client.Products.CreateAsync`, for the invoicing product catalog Mercury added to its API reference.
* `DuplicateCheckOverride` on `SendMoneyAPIRequest` and `PostTransactionAPIRequest`, to send a payment that repeats one from the last 24 hours, and `ReimbursementPaymentStatus.PaidOutsideMercury`.
* An empty, `.` or `..` path value throws `ArgumentException`, and a `null` one `ArgumentNullException`, before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`, or with the `{name}` placeholder left in for `null`.
* An iteration whose cursor returns to a page it already requested, such as page A, then B, then A again, now throws `ApiDecodeException` instead of fetching the same pages until the rate limit runs out. Before, only a cursor that repeated the one just sent was caught.
* A `ListAll…Async` iterator stops at an empty 204 page instead of throwing `ApiDecodeException` partway through `await foreach`.
* A multipart file part sends `filename*` only when the name is not ASCII, and never with quote marks inside it. It used to send the quoted name, so servers that read `filename*` first, such as ASP.NET Core, Django and Werkzeug, kept the quote marks as part of the file name. A `"` or `\` in the name is escaped. An empty name, or one with a control character such as CR or LF, throws `ArgumentException` before anything is sent.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. A new public `ApiJobTimeoutException` carries the last status in `Result` when a job outlasts its timeout. No operation in this package uses either yet.

## 0.1.0-alpha.1 (2026-11-09)

The first alpha.

* Async client for all 87 documented operations, generated from the public spec, targeting .NET 10 and .NET 8.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* `ListAll…Async` iterators on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `IdempotencyKey` is set, which is never changed.
* `MercuryWebhooks.Verify` for the `Mercury-Signature` header.
* PDF downloads ask for `application/pdf` and return the exact bytes.
* Typed exceptions with the status and raw body, and retries and rate-limit handling.
