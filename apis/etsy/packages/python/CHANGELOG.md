# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

## 0.1.0a1 (2026-11-08)

The first alpha.


* Typed sync and async clients for all 107 operations, generated from the public spec.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization URL with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `on_token` callback.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls share one refresh.
* Offset pagination iterators, retries, rate-limit handling, typed errors and redacted logging.
