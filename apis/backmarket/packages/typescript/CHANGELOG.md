# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* Breaking: the `Task` model is `BackgroundTask`, and `TaskActionStatusEnum` is `BackgroundTaskActionStatusEnum`, as in every other language.
* Every method takes options last, with a `signal` that cancels the request and any wait before a retry.
* A call whose `signal` is already aborted sends nothing, and a call aborted after a failed attempt rejects with the signal's reason rather than that failure.
* Each error class has a literal `kind`, and `ClientError` is their union, so comparing `kind` narrows the type.
* An empty success body where the spec declares JSON throws `DecodeError` instead of resolving to `undefined`. Where the spec declares text, it resolves to `""`.

## 0.1.0-alpha.2 (2026-11-07)

* No code changes. Published through npm trusted publishing, with provenance.

## 0.1.0-alpha.1 (2026-11-07)

* Typed client for all 40 operations, generated from the public spec, for Node.js 22 or later, as ESM and CommonJS.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging, with no runtime dependencies.
* `maxRetryWaitMs`: a `Retry-After` above it, 60 seconds by default, throws `RateLimitedError` instead of blocking.
* A `next` link that is not a valid URL throws `DecodeError` instead of a raw `TypeError`.
* Requests send `Accept-Encoding: identity`, because `fetch` accepts a gzip body that ends early and would return partial or empty data.
