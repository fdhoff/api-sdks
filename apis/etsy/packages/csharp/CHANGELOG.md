# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty 204 response returns `null`, even where the spec also declares JSON, instead of throwing `ApiDecodeException`.
* A 401 that raced an explicit `OAuth.RefreshAsync` could send a second token request with the refresh token just issued. It now waits for that refresh and uses its token.
* New public `Download` and `RawBody` types, for binary response and request bodies. No operation in this package uses them yet.
* A file part of a multipart upload is sent with `Content-Type: application/octet-stream`.
* A multipart file part sends `filename*` only when the name is not ASCII, and never with quote marks inside it. It used to send the quoted name, so servers that read `filename*` first, such as ASP.NET Core, Django and Werkzeug, kept the quote marks as part of the file name. A `"` or `\` in the name is escaped. An empty name, or one with a control character such as CR or LF, throws `ArgumentException` before anything is sent.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Async client for all 107 operations, generated from the public spec, targeting .NET 10 and .NET 8.
* `x-api-key` on every call, and the OAuth access token only on calls that need it.
* OAuth 2 helpers: an authorization request with PKCE S256 and state, code exchange and refresh. Each new token pair goes to an `OnToken` callback.
* After a 401, the access token is refreshed once and the call retried. Concurrent calls, and an explicit `OAuth.RefreshAsync`, share one refresh. A failed refresh throws its own error, not the 401.
* Cancelling a call stops its wait for a token request, not the request, so a rotated token pair is not lost. The request is bounded by `Timeout`.
* The current tokens are always redacted. Of earlier tokens and codes only the most recent are kept, so a long-lived client does not grow.
* A null item in a list parameter is skipped instead of throwing.
* Offset pagination as `IAsyncEnumerable`, retries, rate-limit handling, typed exceptions and redacted logging.
