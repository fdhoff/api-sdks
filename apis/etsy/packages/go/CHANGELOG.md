# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty 204 response returns a nil result, even where the spec also declares JSON, instead of an error matching `ErrDecode`.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Typed client for all 107 operations, generated from the public spec, with `context.Context` on every call.
* `x-api-key` on every API call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization request with PKCE S256 and state, code exchange and refresh. Each new token pair goes to the `WithOnToken` function.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `OAuth.Refresh`, share one refresh. A failed refresh returns its own error, not the 401.
* A token request, once sent, finishes even if the caller's context is cancelled, so a rotated token pair is not lost.
* The current tokens are always redacted. Of earlier tokens and codes only the most recent are kept, so a long-lived client does not grow.
* Printing or logging an `AuthorizationRequest` hides its code verifier.
* A params struct with both form-encoded and multipart fields returns an error instead of dropping the form-encoded ones.
* Offset pagination iterators, retries, rate-limit handling, typed errors and redacted logging.
