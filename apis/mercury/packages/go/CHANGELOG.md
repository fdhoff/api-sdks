# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value returns an error before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* An iteration whose cursor returns to a page it already requested, such as page A, then B, then A again, now yields an error matching `ErrDecode` instead of fetching the same pages until the rate limit runs out. Before, only a cursor that repeated the one just sent was caught.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. A wait that reaches its deadline returns an error matching the new `ErrJobTimeout`, with the last status in `APIError.Result`. No operation in this package uses either yet.

## 0.1.0-alpha.1 (2026-11-09)

The first alpha.

* Typed client for all 87 documented operations, generated from the public spec, with `context.Context` on every call.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* Iterators on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `IdempotencyKey` is set, which is never changed.
* `VerifyWebhook` for the `Mercury-Signature` header.
* PDF downloads ask for `application/pdf` and return the exact bytes.
* Typed errors with the status and raw body, and retries and rate-limit handling.
