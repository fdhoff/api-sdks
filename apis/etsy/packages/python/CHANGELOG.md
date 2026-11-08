# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

The first alpha, not yet published.


* Typed sync and async clients for all 107 operations, generated from the public spec.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization URL with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `on_token` callback.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `oauth.refresh()`, share one refresh.
* Only the most recent tokens and codes are kept for redaction, so a long-lived client does not grow.
* Offset pagination iterators, retries, rate-limit handling, typed errors and redacted logging.
