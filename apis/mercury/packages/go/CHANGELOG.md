# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Typed client for all 87 documented operations, generated from the public spec, with `context.Context` on every call.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* Iterators on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `IdempotencyKey` is set, which is never changed.
* `VerifyWebhook` for the `Mercury-Signature` header.
* PDF downloads ask for `application/pdf` and return the exact bytes.
* Typed errors with the status and raw body, and retries and rate-limit handling.
