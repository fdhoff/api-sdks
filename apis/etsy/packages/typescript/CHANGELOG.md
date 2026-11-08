# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* A `Date` in a form field is sent as ISO 8601 text, not as a quoted JSON string.
## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Typed client for all 107 operations, generated from the public spec, for Node.js 22 or later, as ESM and CommonJS, with no runtime dependencies.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization URL with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `onToken` callback, which the call waits for.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `oauth.refresh()`, share one refresh.
* The current tokens are always redacted. Of earlier tokens and codes only the most recent are kept, so a long-lived client does not grow.
* Form bodies are sent form-encoded, with array fields repeated.
* Offset pagination iterators, retries, rate-limit handling, cancellation, typed errors and redacted logging.
* An object in a form-encoded field is sent as JSON, as in the other SDKs, not as `[object Object]`.
