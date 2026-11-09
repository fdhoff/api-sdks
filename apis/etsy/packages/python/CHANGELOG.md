# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* A model in a multipart body is sent as JSON, not as its Python repr, and a mapping is sent as compact JSON.
* An empty, `.` or `..` path value raises `ValueError` before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* A tuple or frozenset passed as an array argument is sent as one value per item, as a list is. Before, it was sent as its Python repr, in query parameters and form fields such as `listings.create_draft`'s `tags`.
* The package ships a `py.typed` marker, so type checkers read its annotations instead of skipping it.
* An empty 204 response now returns `None`, and ends an iteration, instead of raising `DecodeError` where the operation also declares a JSON success.
* Method docstrings show apostrophes as written, not as `&#39;`.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.

## 0.1.0a1 (2026-11-08)

The first alpha.


* Typed sync and async clients for all 107 operations, generated from the public spec.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization URL with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `on_token` callback.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `oauth.refresh()`, share one refresh.
* The current tokens are always redacted. Of earlier tokens and codes only the most recent are kept, so a long-lived client does not grow.
* Offset pagination iterators, retries, rate-limit handling, typed errors and redacted logging.
* A mapping or model in a form-encoded field is sent as JSON, as in the other SDKs, not as its Python repr.
