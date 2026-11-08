# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Typed client for all 107 operations, generated from the public spec, with `context.Context` on every call.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization request with PKCE S256 and state, code exchange and refresh. Each new token pair goes to the `WithOnToken` function.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls share one refresh.
* Offset pagination iterators, retries, rate-limit handling, typed errors and redacted logging.
