# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.

## 0.1.0a1 (2026-11-08)

The first alpha.

* Typed sync and async clients for all 87 documented operations, generated from the public spec.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* Iterators on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `idempotencyKey` is set, which is never changed.
* `verify_webhook` for the `Mercury-Signature` header.
* Typed errors with the status and raw body, and retries and rate-limit handling.
