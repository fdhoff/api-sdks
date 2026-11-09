# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

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
