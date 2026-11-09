# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

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
