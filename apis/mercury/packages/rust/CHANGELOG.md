# Changelog

This crate follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* An async client with typed models for all 87 documented operations, generated from the public spec.
* Your API token as a bearer token on every call, sent verbatim and redacted from errors and logs.
* Production and sandbox environments, with card details fetched from the Vault host.
* Streams on the 26 paged operations: cursor (`start_after`), offset, and the treasury transactions cursor.
* Retries on 5xx, timeouts and dropped connections for the four money-moving writes when their `idempotencyKey` is set, which is never changed.
* `webhooks::verify_webhook` for the `Mercury-Signature` header, behind the default `webhooks` feature.
* Typed errors with the status and raw body, and retries and rate-limit handling.
* PDF downloads ask for `application/pdf`.
