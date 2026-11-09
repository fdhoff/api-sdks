# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value throws `TypeError` before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* An iterator page without its items list throws `DecodeError`, as in the other languages, instead of ending the iteration with no items.
* An empty 204 page ends an iteration instead of throwing `DecodeError`.
* A `Date` in a form field is sent as ISO 8601 text, not as a quoted JSON string.
* Method doc comments show apostrophes as written, not as `&#39;`.
* An iterator page that is a JSON array throws `DecodeError`, as in the other languages, instead of ending the iteration with no items.
* Breaking: the `Task` model is `BackgroundTask`, and `TaskActionStatusEnum` is `BackgroundTaskActionStatusEnum`, as in every other language.
* The repository moved to `fdhoff/api-sdks`; the package's repository and documentation links point there.
* Every method takes options last, with a `signal` that cancels the request and any wait before a retry.
* A call whose `signal` is already aborted sends nothing, and a call aborted after a failed attempt rejects with the signal's reason rather than that failure.
* Each error class has a literal `kind`, and `ClientError` is their union, so comparing `kind` narrows the type.
* An empty success body where the spec declares JSON throws `DecodeError` instead of resolving to `undefined`. Where the spec declares text, it resolves to `""`.
* An empty 204 response resolves to `undefined`, even where the spec also declares JSON, instead of throwing `DecodeError`.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.

## 0.1.0-alpha.2 (2026-11-07)

* No code changes. Published through npm trusted publishing, with provenance.

## 0.1.0-alpha.1 (2026-11-07)

* Typed client for all 40 operations, generated from the public spec, for Node.js 22 or later, as ESM and CommonJS.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging, with no runtime dependencies.
* `maxRetryWaitMs`: a `Retry-After` above it, 60 seconds by default, throws `RateLimitedError` instead of blocking.
* A `next` link that is not a valid URL throws `DecodeError` instead of a raw `TypeError`.
* Requests send `Accept-Encoding: identity`, because `fetch` accepts a gzip body that ends early and would return partial or empty data.
