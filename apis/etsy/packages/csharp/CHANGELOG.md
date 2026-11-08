# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

The first alpha, not yet published.

* Async client for all 107 operations, generated from the public spec, targeting .NET 10 and .NET 8.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization request with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `OnToken` callback.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `OAuth.RefreshAsync`, share one refresh. A failed refresh throws its own error, not the 401.
* Cancelling a call stops its wait for a token request, not the request, so a rotated token pair is not lost. The request is bounded by `Timeout`.
* The current tokens are always redacted. Of earlier tokens and codes only the most recent are kept, so a long-lived client does not grow.
* A null item in a list parameter is skipped instead of throwing.
* Offset pagination as `IAsyncEnumerable`, retries, rate-limit handling, typed exceptions and redacted logging.
