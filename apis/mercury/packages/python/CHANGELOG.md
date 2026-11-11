# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* `client.products.delete`, to delete an invoicing product.
* Request models check the string lengths Mercury now declares, such as 1 to 299 characters for a product name and 1 to 5000 for a customer name, and raise pydantic's `ValidationError` when built outside them. Responses are still read as sent.

## 0.1.0a2 (2026-11-10)

* `client.products.list`, `client.products.iter` and `client.products.create`, for the invoicing product catalog Mercury added to its API reference.
* `duplicate_check_override` on `SendMoneyAPIRequest` and `PostTransactionAPIRequest`, to send a payment that repeats one from the last 24 hours, and `ReimbursementPaymentStatus.PAIDOUTSIDEMERCURY`.
* A model in a multipart body is sent as JSON, not as its Python repr, and a mapping is sent as compact JSON.
* An empty, `.` or `..` path value raises `ValueError` before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* An iteration whose cursor returns to a page it already requested, such as page A, then B, then A again, now raises `DecodeError` instead of fetching the same pages until the rate limit runs out. Before, only a cursor that repeated the one just sent was caught.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.
* A tuple or frozenset passed as an array argument is sent as one value per item, as a list is. Before, it was sent as its Python repr, so a filter such as `cards.list(status=("active", "frozen"))` matched nothing it should.

## 0.1.0a1 (2026-11-08)

The first alpha.

* Typed sync and async clients for all 87 documented operations, generated from the public spec.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* Iterators on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `idempotencyKey` is set, which is never changed.
* `verify_webhook` for the `Mercury-Signature` header.
* Typed errors with the status and raw body, and retries and rate-limit handling.
