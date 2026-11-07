# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* `APIError.Error()` includes the cause, such as the DNS or TLS failure behind "the connection failed", with the token removed. `errors.Is` and `errors.As` still reach the cause.

## 0.1.0-alpha.1 (2026-11-07)

* Typed client for all 40 operations, generated from the public spec, with `context.Context` on every call.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging.
* A request that cannot be encoded is not sent, and returns an error wrapping the encoder's own rather than an `APIError`.
* An optional or single-type union field has its type, such as `Competitor.MinPrice` as `*MonetaryAmount` and `Task.LastActionError` as `*string`, rather than `any`.
