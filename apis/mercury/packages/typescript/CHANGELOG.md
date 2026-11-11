# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* `client.products.delete`, to delete an invoicing product.
* `client.products.list`, `client.products.iter` and `client.products.create`, for the invoicing product catalog Mercury added to its API reference.
* `duplicateCheckOverride` on `SendMoneyAPIRequest` and `PostTransactionAPIRequest`, to send a payment that repeats one from the last 24 hours, and the `paidOutsideMercury` reimbursement payment status.
* Releases are published to npm's `latest` tag instead of `alpha`, so `npm install mercury-banking` gets the newest 0.x release.
* An empty, `.` or `..` path value throws `TypeError` before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* An iteration whose cursor returns to a page it already requested, such as page A, then B, then A again, now throws `DecodeError` instead of fetching the same pages until the rate limit runs out. Before, only a cursor that repeated the one just sent was caught.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.

## 0.1.0-alpha.2 (2026-11-09)

* No code changes. Published through npm trusted publishing, with provenance.

## 0.1.0-alpha.1 (2026-11-09)

The first alpha.

* Typed client for all 87 documented operations, generated from the public spec, for Node.js 22 or later, as ESM and CommonJS, with no runtime dependencies.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* Iterators on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `idempotencyKey` is set, which is never changed.
* `verifyWebhook` for the `Mercury-Signature` header.
* Typed errors with the status and raw body, retries, rate-limit handling, cancellation and redacted logging.
