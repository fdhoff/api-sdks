# Changelog

This crate follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value is an `ErrorKind::Api` error and nothing is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* A POST, PUT or PATCH without a body sends `Content-Length: 0`, as the other languages' HTTP libraries do.
* An empty 204 response returns the type's default, even where the spec also declares JSON, instead of an `ErrorKind::Decode` error.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.
* A file in a multipart body is sent with `Content-Type: application/octet-stream`, as the other languages' HTTP libraries do.
* A pagination stream ends at an empty 204 page instead of failing with an `ErrorKind::Decode` error, as in Python.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. A job still running at the deadline is an `ErrorKind::JobTimeout` error, whose `Error::job_status` holds its last status. No operation in this package uses either yet.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Async client for all 107 operations, generated from the public spec.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization URL with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `on_token` callback.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `oauth().refresh()`, share one refresh.
* The current tokens are always redacted. Of earlier tokens and codes only the most recent are kept, so a long-lived client does not grow.
* A failure to get random bytes for the authorization URL is `ErrorKind::System`, not `InvalidInput`.
* Form-encoded bodies, offset pagination streams, retries, rate-limit handling, typed errors and redacted logging.
