# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (unreleased)

* Typed client for all 40 operations, generated from the public spec, for Node.js 22 or later, as ESM and CommonJS.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging, with no runtime dependencies.
* `maxRetryWaitMs`: a `Retry-After` above it, 60 seconds by default, throws `RateLimitedError` instead of blocking.
* A `next` link that is not a valid URL throws `DecodeError` instead of a raw `TypeError`.
